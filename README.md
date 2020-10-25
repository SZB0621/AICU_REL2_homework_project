# AICU_REL2_homework_project
gitHub repository of team AICU. We collect the data here for the REL2 homework project for the "Deep learning a gyakorlatban Python és LUA alapon" subject. Team members: Ungvárszky Balázs, Moró Márton, Szabó Bence.

Our goal is to achive an accurate lane-following algorithom using the baseline algorithm provided in Duckietown and AIDO (https://docs.duckietown.org/DT19/AIDO/out/embodied_rpl.html). 


## The first step was to creat the simulation environment for the autonomous Duckiebot
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

To creat the necessary docker container you have to follow the commands in the file: env_setup.txt.
1. Pull the provided docker image
```
docker pull duckietown/gym-duckietown
```

2. docker ps -a
```
docker ps -a
```
3. docker start <CONTAINER ID of the pull-ed repo>
```
docker ps -a
```
4. docker ps
```
docker ps -a
```
5. docker exec -it <CONTAINER ID of the pull-ed repo> /bin/bash
```
docker ps -a
```
6. apt update
```
docker ps -a
```
7. apt install python3-pip (press y)
```
docker ps -a
```
8. pip3 install --upgrade pi
```
docker ps -a
```
9. pip3 --version
```
docker ps -a
```
10. pip3 install -e . (in the directory where 'setup.py' is located)
```
docker ps -a
```
11. apt-get install xvfb mesa-utils -y
```
docker ps -a
```
12. apt install -y python3-pip git git-lfs
```
docker ps -a
```
13. apt-get install pkg-config libfontconfig1-dev
```
docker ps -a
```
14. Xvfb :1 -screen 0 1024x768x24 -ac +extension GLX +render -noreset &> xvfb.log &
```
docker ps -a
```
15. export DISPLAY=:1
```
docker ps -a
```
16. python3 ./manual_control.py --env-name Duckietown-udem1-v0
```
docker ps -a
```
