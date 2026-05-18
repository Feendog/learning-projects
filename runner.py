class Runner:
    def __init__(self, name, age, pr_800):
        self.name = name
        self.age = age
        self.pr_800 = pr_800

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my 800m personal record is {self.pr_800}")

    def update_pr(self, new_pr):
        self.pr_800 = new_pr
        print(f"New PR! {self.name} now runs {self.pr_800} for 800m!")

    def training_pace(self, pace_seconds):
        training_seconds = pace_seconds * 1.25
        minutes = int(training_seconds) // 60
        seconds = int(training_seconds) % 60
        print(f"Training pace: {minutes}:{seconds} per mile")

scotty = Runner("Scotty", 15, "1:58.93")
scotty.introduce()
scotty.update_pr("1:56.00")
scotty.introduce()
scotty.training_pace(118)