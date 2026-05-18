pace_seconds = 118  # 1:58 in seconds

training_seconds = pace_seconds * 1.25
minutes = int(training_seconds) // 60
seconds = int(training_seconds) % 60

print(f"Training pace: {minutes}:{seconds} per mile")