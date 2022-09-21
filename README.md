#top
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

# About The Project
## Introduction
This personal project's primary goal is to develop a replica of a roomba with complete autonomy, one that enables the roomba to move around in space on its own without aid from humans. The environment was created using OpenAI mainly because OpenAI Gym doesn't limit development in just one specific way. Our roomba doesn't have a lot of bells and whistles, but it is made to do one thing very well: give a novice roboticist a simple framework for comprehending roomba software development while imitating a genuine roomba function and even though using a real roomba is always advised, a great Python roomba simulator is a fantastic alternative to start with because it is much more approachable.




<p align="right">(<a href="#top">back to top</a>)</p>

## The Goal
The program for our robot will have one clear goal: it will aim to go to a predetermined place while cleaning as much as it can (ie. passing trough a certain space at least once).
The robot will use Q-learning to make judgments that are close to being random. Once a decision has been made, the robot will receive a reward based on how much it cleaned and how long it took. Every iteration the robot will start to take better descisions and hopefully once a good reward algorithm has been found, it will teach itself how to clean in the most efficient and fast way.

<p align="right">(<a href="#top">back to top</a>)</p>

# Configuration

## Control Inputs: Sensors
A robot may be configured in a number of ways to keep an eye on its surroundings. These might include anything from proximity sensors, cameras, light sensors, bumpers, and so on. 
Robots can also communicate with external sensors to obtain information that they are unable to directly monitor themselves.
Our reference robot includes a simulated lidar sensor that fires lasers in all directions in order to detect impediments. 
There are four more "wall sensors" that are placed four ways. The lidar sensor's range and presicion may both be adjusted. You may always install more "wallsensors" and rapidly adjust their range if more are needed.

The robot must make an effort to gauge its own condition as well as that of the surroundings using its sensors. These estimates will never be flawless, but since the robot will rely on them for all of its judgments, they must be at least reasonably accurate.
It makes the following assumptions using its proximity sensors:

* The approach to barriers
* Distance between barriers
* The place of the robot
* The robot's compass direction


The robot must make an effort to gauge its own condition as well as that of the surroundings using its sensors.

<p align="right">(<a href="#top">back to top</a>)</p>

## Control Outputs: Mobility

The target's coordinates are entered into the control program before the robot is turned on, however they might potentially originate from a separate Python application that manages the robot's movements.

We have many of presumptions about how things work. Among the significant ones are:
* The obstacles are never spherical and the landscape is always plain.
* The tires never squeal
* Nothing will ever maneuver the robot.
* There is no failure or incorrect reading from the sensors. (but there is imprecision)


Even if most of these hypotheses are plausible in a home-like setting, circular obstructions could be present. Our obstacle avoidance program is easily implemented, and it moves around barriers by adhering to their perimeter.
 
# Reward Calculation: 
  
Let’s now consider, the robot has a slight chance of dysfunctioning and might take the left or right or bottom turn instead of taking the upper turn in order to get to the green room from where it is now (red room).
Now, the question is how do we enable the robot to handle this when it is out there in the above environment?

![reward_photo](https://blog.floydhub.com/content/images/2019/05/image-22.png)

An environment with an agent (with stochasticity)
This is a situation where the decision making regarding which turn is to be taken is partly random and partly under the control of the robot.
Partly random because we are not sure when exactly the robot might dysfunction and partly under the control of the robot because it is still making a decision of taking a turn on its own and with the help of the program embedded into it. 
Here is the definition of Markov Decision Processes (collected from Wikipedia):


## Enviroment:

The basic structure of the environment is described by the observation_space and the action_space attributes of the Gym Env class.

The observation_space defines the structure as well as the legitimate values for the observation of the state of the environment. The observation can be different things for different environments. The most common form is a screenshot of the game. There can be other forms of observations as well, such as certain characteristics of the environment described in vector form.

Similarly, the Env class also defines an attribute called the action_space, which describes the numerical structure of the legitimate actions that can be applied to the environment.

## Running the robot: 
   Refer to the set crontab timer section:
   [Set crontab timer](#set-crontab-timer)
   
 
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
