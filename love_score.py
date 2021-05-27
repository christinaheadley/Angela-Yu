name1 = input("What is name #1? ")
name2 = input("What is name #2? ")
names = name1.lower() + name2.lower()
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
true = t + r + u + e
love = l + o + v + e
total = int(str(true) + str (love))

if total < 10 and total > 90:
  print("You go together like Coke and Mentos")
elif total >= 40 and total <= 50:
  print("You are alright together.")
else:
  print(f"Your score is {total}.")