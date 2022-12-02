with open('./02/input.txt', 'r') as f:
    strategy_guide = f.readlines()

# Opponent Move: Row, Player Move: Column
#           Rock    Paper   Scissor
# Rock      3
# Paper             3
# Scissor                       3
outcome_matrix = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

shape_reward = [1, 2, 3]

LUT_RPS_1 = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

def reward_function(game_str: str) -> int:
    opponent, player = game_str.replace("\n", "").split(" ")
    opponent_play = LUT_RPS_1[opponent]
    player_play = LUT_RPS_1[player]

    outcome = outcome_matrix[opponent_play][player_play]
    shape_bonus = shape_reward[player_play]

    score = outcome + shape_bonus

    return score

scores = [reward_function(game_str) for game_str in strategy_guide]
total_score = sum(scores)
print(f"Total score for Part 1: {total_score}")

LUT_outcome = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def find_player_shape_score(opponent, outcome) -> int:
    opponent_play = LUT_RPS_1[opponent]
    desired_outcome = LUT_outcome[outcome]

    player_shape_idx = outcome_matrix[opponent_play].index(desired_outcome)  #CPU cycles are cheap, my time is not
    shape_bonus = shape_reward[player_shape_idx]
    return shape_bonus


def reward_function_2(game_str: str) -> int:
    opponent, outcome = game_str.replace("\n", "").split(" ")
    outcome_score = LUT_outcome[outcome]
    shape_score = find_player_shape_score(opponent, outcome)
    score = outcome_score + shape_score
    return score

scores_2 = [reward_function_2(game_str) for game_str in strategy_guide]
total_score_2 = sum(scores_2)
print(f"Total score for Part 2: {total_score_2}")


