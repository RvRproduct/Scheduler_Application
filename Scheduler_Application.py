"""24 HOUR SCHEDULER APPLICATION
You can enter a number of tasks/goals
and how long each task/goal will take
to complete, along with how long you
are going to sleep. It will then calculate
how much time you have left over from those
24hours.
ROBERTO VALENTINO REYNOSO"""


class Goals:
    def __init__(self):
        self.goals = {}

# def_goals will allow for user inputs for each goal
# and then will add that goal and default value of 0
# to an empty dictionary.
    def set_goals(self):
        goal = ""
        another_selection = ""
        while another_selection == "":
            goal = input("Enter a Task/Goal: ")
            self.goals[goal] = 0
            while another_selection.lower() not in ("yes", "y", "no", "n"):
                another_selection = input(
                    "\nAdd another Task/Goal [yes][no]: ")
            if another_selection.lower() in ("yes", "y"):
                another_selection = ""
            elif another_selection.lower() in ("no", "n"):
                break
        for key, value in self.goals.items():
            print(f"{key.upper()}: {value} hrs")
        return self.goals

# set_est_time will go through each item in the dictionary
# and allow you to change the value for each key if its 0.5
# or a whole num.
    def set_est_time(self):
        goals = self.set_goals()
        time = 0

        for key, value in goals.items():
            time = value
            while time == 0:
                try:
                    time = float(input(
                        f"\n{key.upper()}: Enter Est Time for Task/Goal [0.5]|[1->24]: "))
                except (ValueError) as ex:
                    print(
                        "You didn't enter a valid Time please enter a number from [0.5]|[1->24].")
                else:
                    while not time % 0.5 == 0:
                        time = 0
                        print(
                            "\nCan only be from [0.5|a whole number]\nTRY AGAIN")

            goals[key] = time
            for key, value in goals.items():
                print(f"{key.upper()}: {value} hrs")
        return goals


class Schedule:
    def __init__(self):
        self.time_frame = 24

# time_frame_length will calculated sleep, goals/tasks,
# and time left over. If its over 24 hours, the process
# will restart.
    def time_frame_length(self):
        goals = Goals()
        goals_loaded = goals.set_est_time()
        goals_tasks = 0
        time_left_over = 0
        sleep = 0
        while sleep == 0:
            try:
                sleep = float(input("How long will you sleep: "))
                self.time_frame -= sleep
                for key, value in goals_loaded.items():
                    self.time_frame -= value
                    goals_tasks += value
                if self.time_frame > 0:
                    time_left_over = self.time_frame
            except (ValueError) as ex:
                print(
                    "You didn't enter a valid amount please enter a number from [0.5]|[1->24].")
            else:
                while not sleep % 0.5 == 0:
                    sleep = 0
                    print("\nCan only be from [0.5|a whole number]\nTRY AGAIN")
        if sleep + goals_tasks > 24:
            print(f"""\nSleep: {sleep} hrs
Tasks/Goals: {goals_tasks} hrs
You only have 24 hours, if you add
both the Goals/Task and sleep: {sleep + goals_tasks} hrs
it's over 24 hours.\n""")
            main()
        if sleep + goals_tasks <= 24:
            print(f"""\nBased Hourly
{"*" * 30}""")
            for key, value in goals_loaded.items():
                print(f"{key.upper()}: {value}")
            print(f"""{"*" * 30}\nTasks/Goals (Time Combined): {goals_tasks} hrs
Sleep: {sleep} hrs
Time Left Over: {time_left_over} hrs
{"*" * 30}""")


# main will run the app
def main():
    print(f"""DAY SCHEDULER APPLICATION
{"*" * 30}""")
    run = Schedule()
    run.time_frame_length()


if __name__ == "__main__":
    main()
