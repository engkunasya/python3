# Function to calculate Simple Interest
def calculateSI(principle, period, rate):
    SI = (principle * period * rate) / 100
    return SI

# Function to calculate the total amount to be paid
def calculateAmountToBePaid(principle, SI):
    return principle + SI

# Example usage
principle = 1000
period = 1
rate = 6

# Calculate Simple Interest
simple_interest = calculateSI(principle, period, rate)

# Calculate Total Amount to be Paid
total_amount = calculateAmountToBePaid(principle, simple_interest)

print("Simple Interest:", simple_interest)
print("Total Amount to be Paid:", total_amount)

