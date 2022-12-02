with open('./02/input.txt', 'r') as f:
    strategy_guide = f.readlines()

# Opponent Move: Row, Player Move: Column
#       Rock Paper Scissor
# Rock    3    0      6
# Paper   6    3      0
# Scissor 0    6      3
outcome_matrix = [
    [3, 0, 6],
    [6, 3, 0],
    [0, 6, 3]
]

shape_reward = [1, 2, 3]

LUT_RPS = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

def reward_function(game_str: str) -> int:
    opponent, player = game_str.split(" ")
    opponent_play = LUT_RPS[opponent]
    player_play = LUT_RPS[player]

    outcome = outcome_matrix[opponent_play][player_play]
    shape_bonus = shape_reward[player_play]

    score = outcome + shape_bonus

    return score

scores = [reward_function(game_str) for game_str in strategy_guide]
total_score = sum(scores)
print(f"Total score: {total_score}")

