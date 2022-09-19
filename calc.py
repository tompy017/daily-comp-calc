YEAR = 365
DECIMALS = 8


class Calculator:
    """Models a daily-compound calculator."""
    def __init__(self):
        """Inits calculator with the needed variables."""
        self.annual_rate = None
        self.initial_investment = None
        self.period_q = None
        self.time_period = None
        self.total_capital = 0
        self.period_interest = 0
        self.period_earns = []
        self.start()

    def start(self):
        """Prompts for all the variables needed to calculate the interests."""
        self.initial_investment = input("Enter your investment amount: ")
        self.annual_rate = input("Enter the annual interest rate: ")
        self.period_q = input("Enter a period of time for your capital: ")

    def calculate_returns(self):
        """Checks the data provided by the user. If the data is ok, it will
        continue to calculate and inform the period gains. If data there's
        a problem with the data it will ask again to complete all the variables.
        """
        data_checked = False
        while not data_checked:
            try:
                self.total_capital = float(self.initial_investment)
                self.period_interest = (float(self.annual_rate) / 100) / YEAR

                for period_of_time in range(int(self.period_q)):
                    period_gain = self.total_capital * self.period_interest
                    self.period_earns.append(period_gain)
                    self.total_capital += period_gain
                    print(f"Period {period_of_time + 1} out of {self.period_q} earnings: {round(period_gain, DECIMALS)}")

                data_checked = True

            except ValueError:
                print("There was a problem with your data. Please enter only numbers.\n")
                self.start()

    def inform_details(self):
        """Complete detailed information on earnings."""
        print(f"\nInitial investment: {self.initial_investment}")
        print(f"Annual rate: {self.annual_rate}%")
        print(f"Period of time: {self.period_q} days")
        print(f"Total earnings: {round(sum(self.period_earns), DECIMALS)}")
        print(f"Gains + initial investment: {round(self.total_capital, DECIMALS)}")
