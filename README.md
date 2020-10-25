# AICU_REL2_homework_project
gitHub repository of team AICU. We collect the data here for the REL2 homework project for the "Deep learning a gyakorlatban Python és LUA alapon" subject. Team members: Ungvárszky Balázs, Moró Márton, Szabó Bence.

Our goal is to achive an accurate lane-following algorithom using the baseline algorithm provided in Duckietown and AIDO (https://docs.duckietown.org/DT19/AIDO/out/embodied_rpl.html). 


## The first step was to creat the simulation environment for the autonomous Duckiebot
We used and existing duckietown simulation environment, gym-duckietown which was written in pure python/OpenGL (Pyglet).
'''@misc{gym_duckietown,
  author = {Chevalier-Boisvert, Maxime and Golemo, Florian and Cao, Yanjun and Mehta, Bhairav and Paull, Liam},
  title = {Duckietown Environments for OpenAI Gym},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/duckietown/gym-duckietown}},
}
'''

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
