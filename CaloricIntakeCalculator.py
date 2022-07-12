# Dave Alam
# CS361 - Milestone #1

from datetime import date
import time


class MainMenu:

    def __init__(self):
        self.keep_going = True
        self._crunch = DataCruncher()
        self._wait_time = 2.5

    def render_daily_weight_entry(self):

        keep_going = True

        print("--------------------------------Log Your Daily Weight-------------------------------------")
        print("Logging your daily weight takes seconds and allows you to review your weight loss data \n"
              "later and gain valuable insight into your daily caloric intake. Follow the instructions \n"
              "below to log your daily weigh in!")
        print("------------------------------------------------------------------------------------------\n \n")


        while keep_going:

            print("Please enter your weight below in lbs:")
            user_weight = input()

            if self._crunch.valid_weight(user_weight) is True:
                self._crunch.log_daily_weight(user_weight)
                print("You have entered: " + user_weight + " lbs, for date: " +
                      str(date.today()) + "- is this correct? Y/N")
                if self.user_response_is_yes():
                    keep_going = False
                    print("You have successfully logged your daily weight of: " + user_weight +
                          " lbs for date: " + str(date.today()) + "!\n")
                    print("Returning now to the main menu\n")

                    time.sleep(self._wait_time)

            else:
                print("Invalid entry, please enter a valid weight in lbs below:")

    def render_cli(self):
        print("------------------------------------------")
        print("#     DAILY CALORIC INTAKE CALCULATOR    #")
        print("#              by Dave Alam              #")
        print("------------------------------------------\n")

        print("Please choose from the options below:\n")

        print("1. Log today's weight")
        print("2. View past data")
        print("3. Calculate weight average")
        print("4. View the application tutorial")
        print("5. View advanced options")
        print("6. Exit program")

    def render_tutorial(self):

        print("------------------------Caloric Intake Calculator Tutorial--------------------------------")
        print("Hello, and welcome to the Intake Calculator's tutorial page! take a moment to carefully read \n"
              "through each option below to fully take advantage of this app's features and functionalities!\n")
        print("------------------------------------------------------------------------------------------\n \n")

        print("option 1 - choose this to log your day's weight value")
        print("option 2 - this option allows you to view all your previously entered weigh ins")
        print("option 3 - this option allows you to calculate your average weight over a time period")
        print("Option 5 - view advanced options, like importing a .CSV file to enter weight data")
        print("option 6 - allows you to exit the program\n")

        print("Thanks for taking a moment to learn the functions!\n")

        print("Please press Enter when you're ready to return to the main menu")

        user_input = input()
        if "" in user_input:
            print("Returning now to the main menu")
            time.sleep(self._wait_time)
            self.generate_main_menu()

    def generate_main_menu(self):
        while self.keep_going is True:
            self.render_cli()
            user_input = input()

            if user_input == "1":
                self.render_daily_weight_entry()

            if user_input == "4":
                self.render_tutorial()

            if user_input == "6":
                self.exit_program()

    def exit_program(self):
        print("You have chosen to exit the program- are you sure? Y/N")

        if self.user_response_is_yes():
            self.keep_going = False

            print("Thanks for using Caloric Intake Calculator, see you next time!")

        else:
            print("Returning to the main menu now")
            time.sleep(self._wait_time)
            self.generate_main_menu()

    def user_response_is_yes(self):
        response = input()
        if "Y" in response or "y" in response:
            return True
        elif "N" in response or "n" in response:
            return False
        else:
            print("Invalid entry, please try again with a valid entry of Yes or No")


class DayDatum:
    pass


class DataCruncher:

    def __init__(self):
        pass

    def log_daily_weight(self, weight_in_lbs):
        pass

    def valid_weight(self, weight_in_lbs):

        try:
            int(weight_in_lbs)
        except ValueError:
            return False

        return True

    def valid_date(self, date):
        pass

# --------------- TEST AREA -------------- #


p = MainMenu()
p.generate_main_menu()
