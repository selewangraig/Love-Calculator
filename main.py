# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
full_name = name1 + name2

lower_full_name = full_name.lower()

t = lower_full_name.count("t")
r = lower_full_name.count("r")
u = lower_full_name.count("u")
e = lower_full_name.count("e")

true = t + r + u + e

l = lower_full_name.count("l")
o= lower_full_name.count("o")
v = lower_full_name.count("v")
e = lower_full_name.count("e")

love = l + o + v + e

truelove = str(true) + str(love)

if truelove < "10" or truelove > "90":
    print(f"Your score is {truelove}, you go together like coke and mentos.")
elif truelove > "40" or truelove < "50":
    print(f"Your score is {truelove}, you are alright together.")
else:
    print(f"Your score is {truelove}.")

