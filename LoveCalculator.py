# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
toString = name2 + name1
toLower = toString.lower()

t = toLower.count('t')
r = toLower.count('r')
u = toLower.count('u')
e = toLower.count('e')

true = t + r + u + e

l = toLower.count('l')
o = toLower.count('o')
v = toLower.count('v')
e = toLower.count('e')

love = l + o + v + e

score = str(true) + str(love)
score = int(score)


if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")