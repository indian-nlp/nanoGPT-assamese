import os
import pickle
from contextlib import nullcontext
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from model import GPTConfig, GPT
import argparse, random

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

def initialize_and_generate(init_from='resume', out_dir='out-assamese', start="\n", num_samples=1, max_new_tokens=500, temperature=0.1, top_k=200, seed=None, device='cpu', compile=False):
    print("########\n INITIALIZED MODEL \n########")
    
    # Automatically generates seed if not provided
    if seed is None:
        seed = random.randint(0, 2**32 - 1)
    print(f"Using seed: {seed}")
    
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
    torch.backends.cuda.matmul.allow_tf32 = True  # allow tf32 on matmul
    torch.backends.cudnn.allow_tf32 = True  # allow tf32 on cudnn
    device_type = 'cuda' if 'cuda' in device else 'cpu'  # for later use in torch.autocast
    dtype = 'bfloat16' if torch.cuda.is_available() and torch.cuda.is_bf16_supported() else 'float16'
    ptdtype = {'float32': torch.float32, 'bfloat16': torch.bfloat16, 'float16': torch.float16}[dtype]
    ctx = nullcontext() if device_type == 'cpu' else torch.amp.autocast(device_type=device_type, dtype=ptdtype)

    # model
    if init_from == 'resume':
        # Construct the checkpoint path
        ckpt_path = os.path.join(current_dir, out_dir, 'ckpt.pt')
        
        print("ckp_path:", ckpt_path)
        
        # Check if the checkpoint file exists
        if not os.path.exists(ckpt_path):
            raise FileNotFoundError(f"Checkpoint file not found at {ckpt_path}")
        
        # Load the checkpoint
        checkpoint = torch.load(ckpt_path, map_location=device)
        gptconf = GPTConfig(**checkpoint['model_args'])
        model = GPT(gptconf)
        state_dict = checkpoint['model']
        unwanted_prefix = '_orig_mod.'
        for k, v in list(state_dict.items()):
            if k.startswith(unwanted_prefix):
                state_dict[k[len(unwanted_prefix):]] = state_dict.pop(k)
        model.load_state_dict(state_dict)
    elif init_from.startswith('gpt2'):
        # init from a given GPT-2 model
        pass
        # model = GPT2LMHeadModel.from_pretrained(init_from)
        # tokenizer = GPT2Tokenizer.from_pretrained(init_from)

    model.eval()
    model.to(device)
    if compile:
        model = torch.compile(model)  # requires PyTorch 2.0 (optional)

    # look for the meta pickle in case it is available in the dataset folder
    load_meta = False
    if init_from == 'resume' and 'config' in checkpoint and 'dataset' in checkpoint['config']:  # older checkpoints might not have these...
        meta_path = os.path.join(current_dir, 'data', checkpoint['config']['dataset'], 'meta.pkl')
        load_meta = os.path.exists(meta_path)
    if load_meta:
        print(f"Loading meta from {meta_path}...")
        with open(meta_path, 'rb') as f:
            meta = pickle.load(f)
        stoi, itos = meta['stoi'], meta['itos']
        encode = lambda s: [stoi[c] for c in s]

        def decode(l):
            print("INSIDE THE DECODER")
            result = ''
            for i in l:
                char = itos[i]
                if char in ('!', '।', '৷'):  # Check for special characters
                    result += char
                    return result
                result += char
            return result
    else:
        print("Else Part")

    # encode the beginning of the prompt
    if start.startswith('FILE:'):
        with open(start[5:], 'r', encoding='utf-8') as f:
            start = f.read()
    start_ids = encode(start)
    x = (torch.tensor(start_ids, dtype=torch.long, device=device)[None, ...])

    # run generation
    generated_text = ""
    with torch.no_grad():
        with ctx:
            for k in range(num_samples):
                y = model.generate(x, max_new_tokens=max_new_tokens, temperature=temperature, top_k=top_k)
                generated_text += decode(y[0].tolist())
                print(generated_text)
                print('---------------')

    return generated_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample from a trained model")
    parser.add_argument('--init_from', type=str, default='gpt2', help="Initialize from 'resume' or a GPT-2 variant (e.g., 'gpt2-xl')")
    parser.add_argument('--out_dir', type=str, default='out', help="Output directory for checkpoints")
    parser.add_argument('--start', type=str, default="\n", help="Start text for the generation")
    parser.add_argument('--num_samples', type=int, default=1, help="Number of samples to generate")
    parser.add_argument('--max_new_tokens', type=int, default=500, help="Maximum number of new tokens to generate")
    parser.add_argument('--temperature', type=float, default=0.8, help="Temperature for sampling")
    parser.add_argument('--top_k', type=int, default=200, help="Top K tokens to consider for sampling")
    parser.add_argument('--seed', type=int, default=None, help="Random seed for reproducibility")
    parser.add_argument('--device', type=str, default='cpu', help="Device to use for computation")
    parser.add_argument('--compile', action='store_true', help="Whether to compile the model for faster inference")

    args = parser.parse_args()

    generated_output = initialize_and_generate(
        init_from=args.init_from,
        out_dir=args.out_dir,
        start=args.start,
        num_samples=args.num_samples,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_k=args.top_k,
        seed=args.seed,
        device=args.device,
        compile=args.compile
    )
    
    print('#######################\n', generated_output)
