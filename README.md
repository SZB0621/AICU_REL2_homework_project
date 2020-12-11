# AICU REL2 homework project
gitHub repository of team AICU. We collect the data here for the REL2 homework project for the "Deep learning a gyakorlatban Python és LUA alapon" course. 
Team members: 
- Ungvárszky Balázs (Final semester on BME BSC, writing final thesis and having final exams soon), 
- Moró Márton, 
- Szabó Bence (Final semester on BME BSC, writing final thesis and having final exams soon).

## Table of Contents
- [Documentation]()
 - [Abstract]()
 - [Összefoglaló]()
- [Setting up the Environment](https://github.com/SZB0621/AICU_REL2_homework_project#the-first-step-was-to-create-the-simulation-environment-for-the-autonomous-duckiebot)
  - [Requirements for the environment](https://github.com/SZB0621/AICU_REL2_homework_project#the-setup-requires-the-following-components)
  - [Commands for the setup](https://github.com/SZB0621/AICU_REL2_homework_project#commands)
  - [Commands for Virtual Machine](https://github.com/SZB0621/AICU_REL2_homework_project#commands-2)
- [Lane following with Reinforcement Learning](https://github.com/SZB0621/AICU_REL2_homework_project#implementing-lane-following-with-reinforcement-learning)
  - [Training the policy](https://github.com/SZB0621/AICU_REL2_homework_project#start-training-the-baseline-policy)
  - [Requirements for the Training](https://github.com/SZB0621/AICU_REL2_homework_project#extra-requirements)
  - [Commands to start the training](https://github.com/SZB0621/AICU_REL2_homework_project#commands-1)
- [Optimising the algorithm parameters ](https://github.com/SZB0621/AICU_REL2_homework_project#optimising-the-algorithm-parameters)
  - [Chosing the right framework](https://github.com/SZB0621/AICU_REL2_homework_project#chosing-the-right-framework)
  - [Stable baselines solution](https://github.com/SZB0621/AICU_REL2_homework_project#stable-baselines-solution)
  - [What's next?](https://github.com/SZB0621/AICU_REL2_homework_project#whats-next)

## Documentation

The description of the Project, the Learning algorithms and the optimizer algorithm can be found in the [Documentation](https://github.com/SZB0621/AICU_REL2_homework_project/blob/main/Documentation.pdf) file.

Our goal is to achive an accurate lane-following algorithom using the baseline algorithm provided by Duckietown and AIDO frameworks 
(https://docs.duckietown.org/DT19/AIDO/out/embodied_rpl.html). 

### Abstract

This paper describes two solutions to the Duckietown lane following challenge using deep reinforcement learning. In our case Duckietown is a simple environment consisting of roads and green areas. This is where the Duckiebot has to navigate using its camera for lane detection. The solutions are two policy optimization method-based agents. The development was done in an environment with serious limitations but through hyperparameter tuning and other optimizations we achieved increasingly better results. In the following we discuss the DuckieTown framework, environment, the exact building blocks of the agent and how we optimized to use the available computational resources and increase its performance.

### Összefoglaló

## The first step was to create the simulation environment for the autonomous Duckiebot
We used and existing duckietown simulation environment, gym-duckietown which was written in pure python/OpenGL (Pyglet).

```
@misc{gym_duckietown,
  author = {Chevalier-Boisvert, Maxime and Golemo, Florian and Cao, Yanjun and Mehta, Bhairav and Paull, Liam},
  title = {Duckietown Environments for OpenAI Gym},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/duckietown/gym-duckietown}},}
```

### Setting up the environment
#### The setup requires the following components:

- Docker
- Python 3.6+
- pip3
- git, git-lfs
- xvfb
- pkg-config
- OpenAI gym
- NumPy
- Pyglet
- PyYAML
- cloudpickle
- pygeometry
- dataclasses (if using Python3.6)
- PyTorch or Tensorflow (to use the scripts in learning/)

#### Commands:

To create the necessary docker container you have to follow the commands in the file: env_setup.txt.
1. Pull the provided docker image
```
docker pull duckietown/gym-duckietown
```

2. List all of the existing docker images, check that the one you pulled is here
```
docker ps -a
```
3. Run a container of the pulled base image
```
docker start <CONTAINER ID of the pull-ed repo>
```
4. Now your container is running, check it
```
docker ps
```
5. Start using the container
```
docker exec -it <CONTAINER ID of the pull-ed repo> /bin/bash
```
6. Update ubuntu's  Advanced Packaging Tool (APT)
```
apt update
```
7. Install pip
```
apt install python3-pip
```
8. Update pip
```
pip3 install --upgrade pip
```
9. Check if the latest pip3 version is installed
```
pip3 --version
```
10. Install the gym-duckietown's packages, first cd into the diractory where 'setup.py' file is located
```
pip3 install -e . (in the directory where 'setup.py' is located)
```
11. Running the simulator headless (in docker or via SSH) requires virtual frame buffer
```
apt-get install xvfb mesa-utils -y
```
12. Install pip, git and git-lfs
```
apt install -y python3-pip git git-lfs
```
13. Install pkg-config and libfontconfig1-dev to start the simulation
```
apt-get install pkg-config libfontconfig1-dev
```
14. Create a virtual display with OpenGL support 
```
Xvfb :1 -screen 0 1024x768x24 -ac +extension GLX +render -noreset &> xvfb.log &
export DISPLAY=:$SLURM_JOB_ID
```
15. Test the simulator
```
python3 ./manual_control.py --env-name Duckietown-udem1-v0
```
following these commands you should see something like this in terminal(this is a headless mode):

![alt text](https://github.com/SZB0621/AICU_REL2_homework_project/blob/main/image.png?raw=true)

#### Commands 2:
Executing the installations and package updates above in a virtual machine (for exemple: VirtualBox - Ubuntu:18.04) the following points aren't necessary : 1-5,11-14, and some commands require authorization you should use 'sudo' when executing them. 

Depending on the Ubuntu image you may have to install glut as well with the following command:
```
sudo apt-get install freeglut3-dev0
sudo dnf install freeglut-devel
```

After executing the test command you should see something like this in terminal:

![alt text](https://github.com/SZB0621/AICU_REL2_homework_project/blob/main/image2.png?raw=true)
![alt text](https://github.com/SZB0621/AICU_REL2_homework_project/blob/main/image3.png?raw=true)


You can navigate the duckiebot using the built in arrow buttons.

## Implementing Lane following with Reinforcement Learning

### Start Training the baseline Policy (Duckietown's baseline algorithm with DDPG)
#### Extra requirements
##### Software components

- CUDA10.2+ (or CUDA11)

##### Hardware components

- optimal:
  - more than 8GB RAM
  - recent graphic card
- enough:
  - recent CPU
  - 8GB RAM
  
#### Commands:

1. Clone the repo from github which contains the baseline algorithm for the Lane Following challange

```
git clone https://github.com/duckietown/challenge-aido_LF-baseline-RL-sim-pytorch
```
2. Go into the directory
```
cd challenge-aido_LF-baseline-RL-sim-pytorch
```
3. Install the necessary packages:
```
pip3 install -e .
```
4. Now install the gym-duckietown packages:
```
pip3 install -e git://github.com/duckietown/gym-duckietown.git@daffy#egg=gym-duckietown
```
5. Go into the directory where thje training scripts are located and run them
```
cd duckietown_rl
python3 -m scripts.train_cnn.py --seed 123
```
6. When it finishes, test your results in simulation 
```
python3 -m scripts.test_cnn.py --seed 123
```
After executing the training commands you should see something like this:

![alt text](https://github.com/SZB0621/AICU_REL2_homework_project/blob/main/image4.png?raw=true)

Test window:
![alt text](https://github.com/SZB0621/AICU_REL2_homework_project/blob/main/image5.png?raw=true)

The training looks like this in Docker:
![alt text](https://github.com/SZB0621/AICU_REL2_homework_project/blob/main/image6.png?raw=true)

It is visible that the policy is being trained but the rewards are really negative, the following task is hyperparameter optimalization.
After that our agent will be able to stay between the lines with a much higher chance.

## Optimising the algorithm parameters 

After seeing the results of this basic training script with DDPG policy we moved on  to use other toolboxes as we didn't recieve good results and this training script turned out to be very difficult to customize.

The following frameworks were tested:
 - Stable Baselines 3
 - TensorForce
 
 ### Chosing the right framework
 
 We executed several tests and read the documentations of both frameworks and we decided to follow up with Stable Baselines 3. The main reason behind this decision was that SB3 provided several RL algorithms (PPO,DDPG,A2C...), there was an optimizer tool implemented already (Optuna) and this framework used up the least amount of computing capacity.
 
 So we converted all of our previous work inside Stable Baselines 3 framework. The other main change to our project was that we executed and develped the whole project in google collaboratory. This was a necessary step because of the lack of GPU capacity from our side.
 
 ### Stable Baselines solution
 
 Stable Baselines:
 
 ```
 @misc{stable-baselines,
  author = {Hill, Ashley and Raffin, Antonin and Ernestus, Maximilian and Gleave, Adam and Kanervisto, Anssi and Traore, Rene and Dhariwal, Prafulla and Hesse, Christopher and Klimov, Oleg and Nichol, Alex and Plappert, Matthias and Radford, Alec and Schulman, John and Sidor, Szymon and Wu, Yuhuai},
  title = {Stable Baselines},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/hill-a/stable-baselines}},
}
```


Optuna:
```
arXiv:1907.10902 [cs.LG]
```

The executable jupyter notebook is stored in this file: [TeamAICU_LF_Solution_with_SB3_and_Optuna_clean_V1_0](https://github.com/SZB0621/AICU_REL2_homework_project/blob/main/TeamAICU_LF_Solution_with_SB3_and_Optuna_clean_V1_1.ipynb)

There are some requirements regarding our jupyter project, all of them is discussed and installed/imported in the code in [TeamAICU_LF_Solution_with_SB3_and_Optuna_clean_V1_0](https://github.com/SZB0621/AICU_REL2_homework_project/blob/main/TeamAICU_LF_Solution_with_SB3_and_Optuna_clean_V1_1.ipynb)

#### Features in the notebook

 - Installingt the requirements
 - importing the requierements
 - Pptimizer and tester functions (i.e.: CallBacks, optimize_ppo/a2c, pruner, pickle, evaluation...)
 - Models and training policies
 - Plots about the optimizer results, with the given hyperparameters
 
 
 ### What's next?
 
 We will create executable python files for every feature in the jupyter notebook and a dockerfile so that it will be possible to test our project in the real Duckietown-gym environment and execute it with better computing capacity. We intend to test it on a dedicated computer as well.



