name1 = input("What's your name: ").lower()
name2 = input("What's her name: ").lower()
names = name1 + name2

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

total_true = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

total_love = l + o + v + e 

love_score = int(str(total_true) + str(total_love))

if love_score <= 10 or love_score >= 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}") 