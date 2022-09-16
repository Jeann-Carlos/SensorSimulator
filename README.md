<!-- TABLE OF CONTENTS -->
<details>
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
</details>

<!-- ABOUT THE PROJECT -->
<div id="#about-the-project"></div>
## About The Project

The ever-increasing demand for security in the cyberspace environment is
always on the lookout for the safest way to browse the internet without fear of
repercussions. As a result, restrictions are always imposed to prevent malicious
agents from gaining access to our systems. Because of the risks involved, drastic
measures are sometimes taken such as blocking all incoming connections to the
network. Despite there being ways to get around these restrictions, on the rare
occasion that you need to access any restricted network from outside (of their local network), current methods require leaving our system somewhat vulnerable.


This research focuses on creating innovative methods for gaining secure access to
these restricted systems while minimizing any potential hazards involved. The
main scope of this project is to allow those in need of reconnaissance of their
private system to be able to do so without fear of exposing themselves or their
systems. Many governmental and commercial enterprises may find it advantageous to be able to open up their network without granting the entire access
to it and/or exposing it to outsiders. Plausible scenarios where our research
could help is in the incorporation of third-party IT/Network management users
or networks that may be located behind many firewalls.This is currently being
accomplished through the usage of VPNs and traffic redirection but other
methods are planned.


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->

## Getting Started

This is a reference page designed to assist anyone working on this project with setting up the basics and getting their computers up and running. It is assumed that you are familiar with bash commands and terminal usage.For this project, only two debian-based machines are required: the server and the client, where as the client must be situated within the restricted network.


<p align="right">(<a href="#top">back to top</a>)</p>


## Prepared ISO installation:
 
#### Download the ISO for the respective machines:
   1. Link to the server mahcine iso: [https://example.com](https://example.com)  
     User: cslab  
     Pass: sweet child o ccom
   2. Link to the client mahcine iso: [https://example.com](https://example.com)  
      User: cslab  
      Pass: sweet child o ccom  
  #### Clone the project: 
   Once you are in, use the terminal to clone the project:
   ```
   git clone https://git.ccom.uprrp.edu/jeann.hernandez/cslabproject.git
   ```  
   
   
### Server Side:  
   If you dont have a VPN of your own, you can use the openvpn installer:
   ```
   sudo chmod +x ./cslabproject/server_workdir/openvpn_install.sh
   sudo ./cslabproject/server_workdir/openvpn-install.sh
   ```
#### Setup Crontab: 
   Refer to the set crontab timer section:
   [Set crontab timer](#set-crontab-timer)
   
  
  
### Client Side:
   Run the installation script with your respective ovpn key:
   ```
   sudo chmod +x ./cslabproject/client_workdir/installation_script.sh
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


## Manual Installation:

  Download the ISO for their respective machines:
   1. Link to the server mahcine iso: [https://example.com](https://example.com)  
     User: cslab  
     Pass: sweet child o ccom
   3. Link to the client mahcine iso: [https://example.com](https://example.com)  
    User: cslab  
    Pass: sweet child o ccom
  Clone the project: 
   Once you are in, use the terminal to clone the project:
   ```
   git clone https://git.ccom.uprrp.edu/jeann.hernandez/cslabproject.git
   ```
   

### Server Side:
#### Run the installation script:  
   ```
   sudo chmod +x ./cslabproject/server_workdir/installation_script.sh
   sudo ./cslabproject/server_workdir/installation_script.sh
   ```
   If you dont have a VPN of your own, you can use the openvpn installer:
   ```
   sudo chmod +x ./cslabproject/server_workdir/openvpn_install.sh
   sudo ./cslabproject/server_workdir/openvpn-install.sh
   ```
#### Set up the Database:
   ```  
   sudo mysql -u root
   ```
   Inside mysql:  
   ```
   create database [DB_name];
   use [DB_name];
   ```
   Copy generated sources from `genSources.txt` located in `cslab/server_workdir/genSources.txt`.  
   And run
   ```
  show tables;
   ```
#### Create a new DB user:
   ```
 CREATE USER '[user_name]'@'localhost' IDENTIFIED BY '[password]';
   ```
   To assign privileges to your database:
   ```
 GRANT ALL PRIVILEGES ON [DB_name].* TO '[user_name]'@localhost IDENTIFIED BY '[password]';
   ```
   Exit MariaDB:
   ```
 exit
   ```
#### Create new user for RRsync (Restricted rsync):
 To add the user run: 
  ```
sudo useradd [rrsync_user]
  ```
 To add password to it:
   ```
sudo passwd  [rrsync_user]
   ```
  Assing a home dir:
   ```
sudo mkhomedir_helper [rrsync_user]
   ```
   Create a results dir in their home dir and correct permissions:
   ```
   sudo mkdir /home/[rrsync_user]/results
   sudo chown [rrsync_user] /home/[rrsync_user]/results
   sudo chmod 755 /home/client_rrsync/results
   ```
#### Setup User quota:
   Modify sudo nano `/etc/fstab modify` the `options` section, add `usrquota grpquota` to it,
   it should look like this.  
##### Example before:  
   
     UUID          /                 ext4    defaults        0 1

##### Example after:    
     UUID          /                  ext4    defaults,usrquota,grpquota  0 1
   Reboot the machine.
   
   After booting run to set user quota with:
   ```
   sudo quotacheck -cum /
   sudo quotaon -v /
   sudo setquota -u [rrsync_client] 1G 1G 0 0 /
   ```
#### Setup Crontab: 
   Refer to the set crontab timer section:
   [Set crontab timer](#set-crontab-timer)
   

### Client Side: 
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
