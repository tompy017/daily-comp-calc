YEAR = 365
DECIMALS = 8


class Calculator:
    def __init__(self):
        self.annual_rate = None
        self.initial_investment = None
        self.period_q = None
        self.total_capital = 0
        self.period_interest = 0
        self.period_earns = []
        self.start()

    def start(self):
        self.initial_investment = input("Enter your investment amount: ")
        self.annual_rate = input("Enter the annual interest rate: ")
        self.period_q = input("Enter a period of time for your capital: ")

    def calculate_returns(self):
        self.total_capital = float(self.initial_investment)
        self.period_interest = (float(self.annual_rate) / 100) / YEAR
        for period_of_time in range(int(self.period_q)):
            period_gain = self.total_capital * self.period_interest
            self.period_earns.append(period_gain)
            self.total_capital += period_gain
            print(f"Period {period_of_time + 1} out of {self.period_q} earnings: {round(period_gain, DECIMALS)}")

    def valid_data(self):
        data_to_check = [self.initial_investment, self.annual_rate, self.period_q]
        try:
            for data in data_to_check:
                float(data)
            return True
        except ValueError:
            print("There was a problem with your data. Please enter only numbers.")
            return False

    def inform_details(self):
        print(f"\nInitial investment: {self.initial_investment}")
        print(f"Annual rate: {self.annual_rate}%")
        print(f"Period of time: {self.period_q}t")
        print(f"Total earnings: {round(sum(self.period_earns), DECIMALS)}")
        print(f"Gains + initial investment: {round(self.total_capital, DECIMALS)}")
