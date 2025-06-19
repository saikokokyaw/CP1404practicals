data = [['Derek', 71], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

# Step 1: Find the longest name for alignment
max_name_length = max(len(name) for name, _ in data)

# Step 2: Print each line with aligned name and score
for name, score in data:
    print(f"{name:<{max_name_length}} = {score:>3}")