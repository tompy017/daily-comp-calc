"""Script to calculate in details the compound interest rate for a given period of days."""

investment = float(input("Enter your investment amount: "))
annual_interest = float(input("Enter the annual interest rate: "))
investment_period = int(input("Enter a period of time (in days): "))
YEAR = 365

daily_interest = (annual_interest / 100) / YEAR

earnings = investment
daily_earnings = []

print("\nTheese would be your returns:")
for day in range(investment_period):
    day_gain = earnings * daily_interest
    daily_earnings.append(day_gain)
    earnings *= 1 + daily_interest
    print(f"Day {day + 1} out of {investment_period} earnings: {round(day_gain,2)}")

print(f"\nInitial investment: {investment}")
print(f"Annual rate: {annual_interest}")
print(f"Days: {investment_period}")
print(f"Total earnings: {round(sum(daily_earnings), 2)}")
print(f"Gains + Investment: {round(earnings, 2)}")
