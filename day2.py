print("Welcome to the tip Calculator.")

bill = float(input("What was the total bill? $ "))

tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

number_of_people = int(input("How many people to split the bill? "))

total_bill_plus_tip = bill + (bill * (tip / 100))
total_for_each_person = str(round(total_bill_plus_tip / number_of_people, 2))

print("Each person should pay:  $%s" % total_for_each_person)