import random
from kaggle_environments.envs.rps.utils import get_score

last_react_action = None


def linear_agent(observation, configuration):
    global last_react_action
    if observation.step == 0:
        last_react_action = random.randrange(0, configuration.signs)
    elif get_score(last_react_action, observation.lastOpponentAction) <= -1:
        last_react_action = (last_react_action + 1) % 3
    return last_react_action
