print ("Welcom to Python Pizza Deliveries!")
size = input("What size pizza do you wnat? s,m,l: ")
add_pepperoni = input("Do you want pepperoni? ")
extra_cheese = input("Do you want extra chesse? ")

bill = 0

if size == "s":
  bill += 15
  if add_pepperoni == "y":
    bill += 2
elif size == "m":
  bill += 20
  if add_pepperoni == "y":
    bill += 3
elif size == "l":
  bill += 25
  if add_pepperoni == "y": 
    bill += 3
else:
  print("Invalid size")

if extra_cheese == "y":
  bill += 1

print(f"Your final bill is : ${bill}")