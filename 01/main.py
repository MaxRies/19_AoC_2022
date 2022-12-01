max_calories = 0

with open('./01/input.txt', 'r') as f:
    current_calories = 0
    for line in f:
        if line == '\n':
            if current_calories > max_calories:
                max_calories = current_calories
                print(f"New highscore: {max_calories}")
            current_calories = 0
        else:
            current_calories += int(line)

print(f"Max Calories: {max_calories}")