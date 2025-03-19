total_bill = float(input("What was the total bill? "))
percentage_tip = int(input("What perventage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total_bill *= 1 + (percentage_tip / 100)
bill_per_person = total_bill / people
print(f"Each person should pay: {round(bill_per_person,2)}")