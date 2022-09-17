<!-- TABLE OF CONTENTS -->

<summary><h2>Table of Contents</h2></summary>
<ol>
<li>
<a href="#about-the-project">About The Project</a>
</li>
<li>
<a href="#getting-started">Getting Started</a>
</li>
<li>
<a href="#prepared-iso-installation">Prepared ISO installation</a>
<ul>
<li><a href="#server-side">Server Side</a></li>
<li><a href="#client-side">Client Side</a></li>
</ul>
</li>
<li>
<a href="#manual-installation">Manual Installation</a>
<ul>
<li><a href="#server-side-1">Server Side</a></li>
<li><a href="#client-side-1">Client Side</a></li>
</ul>
</li>
<li><a href="#set-crontab-timer">Set Crontab timer</a></li>
<li><a href="#usage">Usage</a></li>
<li><a href="#roadmap">Roadmap</a></li>
<li><a href="#contributing">Contributing</a></li>
<li><a href="#license">License</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#acknowledgments">Acknowledgments</a></li>
</ol> 


<!-- ABOUT THE PROJECT -->
<div id="#about-the-project"></div>

## About The Project
Python was used to write the simulator that I created. It does not have many frills, but it is designed to accomplish one thing very well: offer a realistic simulation of a mobile robot and give a budding roboticist a straightforward foundation for learning robot software programming. Although playing with a real robot is always preferable, a solid Python robot simulator is considerably more approachable and a fantastic place to start.
A Q-learning machine algorithm randomly chooses each action the robot does once it has started off at a certain location in the environment. The Q-learning method uses model-free reinforcement learning to determine the worth of a given action in a given situation.
It can handle issues with stochastic transitions and rewards without the need for modifications since it does not require a model of the environment (thus the term "model-free").



<p align="right">(<a href="#top">back to top</a>)</p>



## Control Inputs: Sensors
A robot can be outfitted to monitor its environment in a variety of ways. These might include anything from light sensors, bumpers, cameras, proximity sensors, and so on. Robots can also connect with outside sensors to get data that they themselves are unable to directly monitor.
In order to recognize barriers, our reference robot has a simulated lidar sensor that fires lasers in all directions. There are 4 more "wall sensors" that are oriented in each of the four directions. The lidar sensor's range and presicion may both be adjusted.  If more "wallsensors" are required, you may always add more and quickly change their range.


<p align="right">(<a href="#top">back to top</a>)</p>

## Control Outputs: Mobility

We have many of presumptions about how things work. Among the significant ones are:
* The obstacles are never spherical and the landscape is always plain.
* The tires never squeal
* Nothing will ever maneuver the robot.
* There is no failure or incorrect reading from the sensors. (but there is imprecision)


Even if most of these hypotheses are plausible in a home-like setting, circular obstructions could be present. Our obstacle avoidance program is easily implemented, and it moves around barriers by adhering to their perimeter.

### Running the program: 
#### Prerequisites
 You'll need a machine on a restricted network, preferably running a Debian-based Linux distribution, as well as access to the following programs::
  ```
  curl
  rsync
  enum4linux
  feroxbuster
  gobuster
  impacket-scripts
  nbtscan
  nikto
  nmap
  onesixtyone
  oscanner
  redis-tools
  smbclient
  smbmap
  snmpwalk
  sslscan
  svwar
  tnscmd10g
  whatweb
  wkhtmltopdf
  python
  openvpn
  ```
My recommendation is to use kali linux: https://www.kali.org/get-kali/

#### Run the installation script:  


   Change the apropiate permissions:
   ```
   sudo chmod 755 ./cslabproject/client_workdir/installation_script.sh
   ```
   The file should have a variable named `serverip` assing to it your vpn ip like so:
   ```
   serverip=127.0.0.1
   ```
   Run the installation script with your respective ovpn key:
   ```
   sudo ./cslabproject/client_workdir/installation_script.sh [ovpn_key]
   ```   
#### Client_scan settings:  
   Open the file `client_scan.sh` inside client_workdir with a file editor and modify: 
   ```
   localip  # local machine ip
   serverip # vpn server ip
   targettimeout # per target timeout
   globaltimeout # global timeout 
   userrsync # user to rrsync
   ```
#### Setup Crontab: 
   Refer to the set crontab timer section:
   [Set crontab timer](#set-crontab-timer)
   
 
 <p align="right">(<a href="#top">back to top</a>)</p>
 

## Set crontab timer:  
   
   ```
   sudo crontab -e 
   ```
  This line should appear at the end of the file when you open it (unless you used your own ISO): `*/3 * * * * program_name >/dev/null 2>&1`   
   Server: Change it to specify when the process should look for fresh files sent by the client pc; the scan will run every 3 minutes by default.
   Client: Change it to specify when the process should start a scan and send files to the Vpn server.
   
   Crontab Syntax:  
   ![GitHub Logo](https://i2.wp.com/www.adminschoice.com/wp-content/uploads/2009/12/crontab-layout.png?resize=768%2C341&ssl=1)
  
<p align="right">(<a href="#top">back to top</a>)</p>
<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>


<div id="#roadmap"></div>
<!-- ROADMAP -->
## Roadmap

- [ ] More seamless instalation
- [ ] Automatic Vulnerabilty assesement


<p align="right">(<a href="#top">back to top</a>)</p>



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

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
