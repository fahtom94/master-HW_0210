import numpy as np

from kaggle_environments import evaluate


list_names = [
    "agents/copy_opponent",
    "agents/paper_agent",
    "agents/random_agent",
    "agents/random_agent_repeat_action_if_won",
    "agents/repeat_action_if_equal_last_lap_agent",
    "agents/repeat_action_if_lose_last_lap_agent",
    "agents/repeat_action_if_won_last_lap_agent",
    "agents/rock_agent",
    "agents/scissors_agent",
    "agents/simple_linear_agent",
    "agents/simple_statistics_agent",
    "agents/simple_won_linear_agent"
]
list_agents = [agent_name + ".py" for agent_name in list_names]

n_agents = len(list_names)

scores = np.zeros((n_agents, n_agents), dtype=np.int)

print("Simulation of battles. It can take some time...")

for idx_agent_1 in range(len(list_names)):
    for idx_agent_2 in range(idx_agent_1 + 1, len(list_names)):
        print(
            f"LOG: {list_names[idx_agent_1]} vs {list_names[idx_agent_2]}",
            end="\r"
        )

        current_score = evaluate(
            "rps",
            [list_agents[idx_agent_1], list_agents[idx_agent_2]],
            configuration={"episodeSteps": 1000}
        )

        scores[idx_agent_1, idx_agent_2] = current_score[0][0]
        scores[idx_agent_2, idx_agent_1] = current_score[0][1]

    print()

results = {}
for idx_agent_1 in range(len(list_names)):
    win_result = 0
    for idx_agent_2 in range(len(list_names)):
        win_result += scores[idx_agent_1][idx_agent_2]
    results[list_names[idx_agent_1]] = win_result

print("All Results: {}", results)

key_max_val = None
max_val = None
for key, value in results.items():
    if max_val is None:
        max_val = value
        key_max_val = key
    elif value > max_val:
        max_val = value
        key_max_val = key

print("The best agent name: {} with score: {}".format(key_max_val, max_val))