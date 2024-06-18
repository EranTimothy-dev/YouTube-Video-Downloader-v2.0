<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="images/icon.ico" alt="Logo" width="80" height="80">
  

  <h3 align="center">YouTube Video Downloader</h3>
  <br><br>
</div>



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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


This project is an improved version of my previous youtube video downloading project. The main functionality is similar to the old version where it basically allows users to download youtube videos by entering the url, but this version does not download progressive streams like the previous version instead supports only DASH streams.
The video and audio files are downloaded separately and merged to create the final video and saved to the Downloads folder.

Major changes in this version:
* The code base has been modularized for better readability and maintainability.
* The code base is built on the most basic principles of OOP where sections are divided into two main classes and a few modules as well.
* The user can now select from all available resolution qualities available for te video.
* Some improvements have been made to improve the look and feel of the UI.
* Transition from progressive streams to DASH streams.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

The language used to build this project is python. The requirements to run this project is listed in the requirements.txt folder
<br>
In addition to the dependencies users will have to also install ffmpeg. The installation process is explained below. 

* [![Python][python-url]][python]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In order to make the best of this project the following steps will have to be followed carefully. I would recommend to use a virtual environment to run the project ho ever i you wish to run it locally that is also fine.

### Installation

Firstly you will have to clone repo and then install the required dependencies mentioned in the 'requirements.txt' file, copy past the below command to do so.
* Clone the repo
   ```sh
   git clone https://github.com/EranTimothy-dev/YouTube_Video_Downloader_V2.0.git
   ```
* pip
  ```pip
  pip install -r requirements.txt
  ```

Next you will have to locally install ffmpeg in your local system in order to to merger the audio and video file. 

* To install ffmpeg you can follow the below tutorial link:
https://www.wikihow.com/Install-FFmpeg-on-Windows

* After following the installation process you must copy the ffmpeg.exe file in the bin folder inside the ffmpeg file to the packages folder inside the cloned project directory.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To use the program simply open the SearchVideo.py file and run it, afterwards follow the steps instructed in the program.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Create search bar UI
- [x] Program search functionality
- [x] Create the download section UI
- [x] Program the download functionality
- [x] Improve UI features and user experience
- [x] Program the functionality to merge audio and video files
- [x] Cleanup program to automate removing the separate audio and video files


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Your Name - [@linkedIn](https://www.linkedin.com/in/eran-perera-112a8a219) - eranperera.dev@gmail.com

Project Link: [https://github.com/EranTimothy-dev/YouTube_Video_Downloader_V2.0](https://github.com/EranTimothy-dev/YouTube_Video_Downloader_V2.0)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [pytube documentation](https://pytube.io/en/latest/user/quickstart.html)
* [ffmpeg documentation](https://www.webpagefx.com/tools/emoji-cheat-sheehttps://ffmpeg.org/about.html)
* [wikihow](https://www.wikihow.com/Install-FFmpeg-on-Windows)
* [geeksforgeeks](https://ffmpeg.org/about.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python-url]: https://www.python.org/
[python]: https://miro.medium.com/v2/resize:fit:1400/1*m0H6-tUbW6grMlezlb52yw.png