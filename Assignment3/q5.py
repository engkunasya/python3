total_investment = 30000
interest_a = 0.05
interest_b = 0.07
total_profit = 1800

#x = (1800 - 30000 * interest_b) / (interest_a - interest_b)

total_a = (total_profit - total_investment * interest_b) / (interest_a - interest_b)
total_b = total_investment - total_a
print(f"Total amount invested in the first account is: RM{total_a}")
print(f"Total amount invested in the second account is: RM{total_b}")

# print ("a and b are diff") if (total_b == total_a) else print ("they are different")
