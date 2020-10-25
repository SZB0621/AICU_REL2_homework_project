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
1. docker pull duckietown/gym-duckietown
2. docker ps -a
3. docker start <CONTAINER ID of the pull-ed repo>
4. docker ps
5. docker exec -it <CONTAINER ID of the pull-ed repo> /bin/bash
6. apt update
7. apt install python3-pip (press y)
8. pip3 install --upgrade pi
9. pip3 --version
10. pip3 install -e . (in the directory where 'setup.py' is located)
11. apt-get install xvfb mesa-utils -y
12. apt install -y python3-pip git git-lfs
13. apt-get install pkg-config libfontconfig1-dev
14. Xvfb :1 -screen 0 1024x768x24 -ac +extension GLX +render -noreset &> xvfb.log &
15. export DISPLAY=:1
16. python3 ./manual_control.py --env-name Duckietown-udem1-v0
