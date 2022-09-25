import random
from kaggle_environments.envs.rps.utils import get_score

last_react_action = None


def repeat_action_if_lose_last_lap_agent(observation, configuration):
    global last_react_action
    if observation.step == 0:
        last_react_action = random.randrange(0, configuration.signs)
    elif get_score(last_react_action, observation.lastOpponentAction) == 0:
        pass
    else:
        last_react_action = random.randrange(0, configuration.signs)

    return last_react_action
