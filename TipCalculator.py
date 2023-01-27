print("Welcome to the lunch Calculator\n")
print("----------------------------------------------------------------------")
billAmount = float(input("What was the bill amount.\n"))
tipAmount = float(input("What % tip do you want to give\n"))
peopleAmount = float(input("How many people is the bill being split into\n"))
print("----------------------------------------------------------------------\n\n")
finalAmount = billAmount + billAmount*(tipAmount/100) / peopleAmount
print (f"The final pay amount split between {int(peopleAmount)} people, with a tip of {int(tipAmount)}% is {round(finalAmount, 2)}")

