<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/indian-nlp/nanoGPT-assamese">
    <img src="https://raw.githubusercontent.com/indian-nlp/nanoGPT-assamese/main/ss/ico.png" alt="Logo" height="50">
  </a>

<h3 align="center">NanoGPT Assamese</h3>

  <p align="center">
    NanoGPT trained on Assamese dataset
    <br />
    <a href="https://github.com/indian-nlp/nanoGPT-assamese/blob/main/README.md"><em>Releasing Soon to Public </em></a> 
    <br />
    <a href="https://github.com/indian-nlp/nanoGPT-assamese/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/indian-nlp/nanoGPT-assamese/issues">Report Bug</a>
    ·
    <a href="https://github.com/indian-nlp/nanoGPT-assamese/issues">Request Feature</a>
  </p>
</div>

## Screenshots

<img src="https://raw.githubusercontent.com/indian-nlp/nanoGPT-assamese/main/ss/ss1.png">

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

(#about-the-project)

Assamese or Asamiya is an Indo-Aryan language spoken mainly in the north-eastern Indian state of Assam, where it is an official language. It serves as a lingua franca of the wider region and has over 15 million native speakers according to Ethnologue.

This project aims to train the nanoGPT using an Assamese language dataset. 

Contributions are welcome! Please see the [Contributing](#contributing) section to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* nanoGPT
* dataset: arambhani.txt 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To run this code locally, follow these steps.

### Prerequisites

* Web Browser

### Installation

1. Clone the repo
    ```
    git clone https://github.com/indian-nlp/nanoGPT-assamese.git
    ```
2. Go to the project repo folder
    ```
    cd path\to\directory
    ```
3. Create Virtual Env (Recommended)
    ```
    virtualenv venv_name
    ```
4. Install the required Python packages using pip
    ```
    pip install -r 'requirements.txt'
    ```
5. Run the sample.py file to get the sample of the model
    ```
    python sample-old.py --out_dir=out-assamese --device=cpu
    ```
    or, provide a starting text to generate from:
    ```
    python sample-old.py --out_dir=out-assamese --device=cpu --start=কৃতাঞ্জলি
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

See the [open issues](https://github.com/indian-nlp/nanoGPT-assamese/issues) for a list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are welcome! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Don't forget to give the project a star! Thank you!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Sagar Tamang - [LinkedIn](https://www.linkedin.com/in/sagar-tmg/) - cs22bcagn033@kazirangauniversity.in

Official Website: [https://sagartamang.com](https://sagartamang.com)

Project Link: [https://github.com/indian-nlp/nanoGPT-assamese](https://github.com/indian-nlp/nanoGPT-assamese)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* I would like to thank [ChatGPT](https://chat.openai.com/) for helping me debug all the errors.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/indian-nlp/nanoGPT-assamese.svg?style=for-the-badge
[contributors-url]: https://github.com/indian-nlp/nanoGPT-assamese/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/indian-nlp/nanoGPT-assamese.svg?style=for-the-badge
[forks-url]: https://github.com/indian-nlp/nanoGPT-assamese/network/members
[stars-shield]: https://img.shields.io/github/stars/indian-nlp/nanoGPT-assamese.svg?style=for-the-badge
[stars-url]: https://github.com/indian-nlp/nanoGPT-assamese/stargazers
[issues-shield]: https://img.shields.io/github/issues/indian-nlp/nanoGPT-assamese.svg?style=for-the-badge
[issues-url]: https://github.com/indian-nlp/nanoGPT-assamese/issues
[license-url]: https://github.com/indian-nlp/nanoGPT-assamese/blob/master/license.txt
[license-shield]: https://img.shields.io/github/license/indian-nlp/nanoGPT-assamese.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/sagar-tmg/
