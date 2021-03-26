# Weight in lbs
weight = float(input("What is the weight of your package in lbs? "))

# Charge in CAD $
cost = 2.00
charge = 20.00

# Do they want premium?
premium_ask = input("Would you like to upgrade to Premium? ")

if premium_ask == "Yes":
  premium_status = True
elif premium_ask == "No":
  premium_status = False
else:
  print("Sorry, please choose Yes or No")
  input("Would you like to upgrade to Premium? ")

premium = 125.00


# Ground Shipping
if weight <= 2:
  cost =  1.50
elif (weight >= 2) and (weight <= 6):
  cost = 3.00
elif (weight >= 6) and (weight <= 10):
  cost = 4.00
elif (weight >= 10):
  cost = 4.75
else:
  print("Error, please set package weight.")
  
print("The cost based on weight is $", cost)

cost = (cost * weight) + charge
print ("Cost subtotal is $", cost)

if premium_status == True:
  total = cost + premium
  print("Your premium total will be $", total)
else: 
  print("Your non-premium total will be $", cost)