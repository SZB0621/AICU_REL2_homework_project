import os

import numpy as np
import matplotlib.pyplot as plt

from gym import envs
import gym

import gym_duckietown.envs.duckietown_env
env1 = 'Duckietown-small_loop-v0'   #Small loop map
env2 = 'Duckietown-udem1-v0'        #More complex urbun environment
env3 = 'Duckietown-straight_road-v0'#Straight road map

from stable_baselines3 import PPO, A2C #Algorithm and policy import 
from stable_baselines3.ppo.policies import CnnPolicy
from stable_baselines3.a2c.policies import CnnPolicy
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.evaluation import evaluate_policy

import optuna
import joblib as joblib

from optuna.samplers import TPESampler

#PPO optimizer function

def optimize_ppo(trial):
  #Adjust hyperparams 
    """ Learning hyperparamters we want to optimise"""
    return {
        'n_steps': int(trial.suggest_int('n_steps', 32, 512)),
        'gamma': trial.suggest_loguniform('gamma', 0.9, 0.9999),
        'learning_rate': trial.suggest_loguniform('learning_rate', 1e-5, 1e-3),
        'ent_coef': trial.suggest_loguniform('ent_coef', 1e-8, 1e-1),
        'n_epochs': trial.suggest_int('n_epochs',3,5)
    }
    
    #Agent optimizer function for PPO

def optimize_agent(trial):
    """ Train the model and optimise
        Optuna maximises the negative log likelihood, so we
        need to negate the reward here
    """
    model_params = optimize_ppo(trial)
    env = gym.make('Duckietown-straight_road-v0')
    #env = gym.make('Duckietown-small_loop-v0')
    #For multiprocessing
    #env = SubprocVecEnv([lambda: gym.make('Duckietown-small_loop-v0') for i in range(n_cpu)])
    model = PPO(CnnPolicy, env1, verbose=0, **model_params)
    model.learn(1000)

    rewards = []
    n_episodes, reward_sum = 0, 0.0

    obs = env.reset()
    while n_episodes < 10000:
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)
        reward_sum += reward

        if done:
            rewards.append(reward_sum)
            reward_sum = 0.0
            n_episodes += 1
            obs = env.reset()

    last_reward = np.mean(rewards)
    trial.report(-1 * last_reward, n_episodes)

    #Handle pruning based on the intermediate value.
    if trial.should_prune():
      raise optuna.TrialPruned()

    return -1 * last_reward
  
sampler = TPESampler(seed=3) 

study = optuna.create_study(pruner=optuna.pruners.PercentilePruner(percentile=50,n_startup_trials=20,n_warmup_steps=10000,interval_steps=1),sampler=sampler,)
study.optimize(optimize_agent, n_trials=1000, gc_after_trial=True,catch=(float('nan'),))
print(study.best_params)