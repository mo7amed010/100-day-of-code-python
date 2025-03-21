number = int(input("Enter a number to check: "))

if number % 2 == 0:
  print("It's even")
else:
  print("It's odd")

# another way
print("even" if number % 2 == 0 else "odd")