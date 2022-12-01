calory_sums = []

with open('./01/input.txt', 'r') as f:
    current_calories = 0
    for line in f:
        if line == '\n':
            calory_sums.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)

calory_sums.sort()
calory_sums.reverse()
top_three = calory_sums[0:3]
top_three_sum = sum(top_three)
print(f"Sum: {top_three_sum}")