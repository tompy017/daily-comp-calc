"""Script to calculate in details the compound interest rate for a given period of days."""
from calc import Calculator

calculator = Calculator()

while not calculator.valid_data():
    calculator.start()

calculator.calculate_returns()
calculator.inform_details()
