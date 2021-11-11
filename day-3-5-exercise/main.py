# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1=name1.lower()
name2=name2.lower()

t=name1.count("t")
r=name1.count("r")
u=name1.count("u")
e=name1.count("e")
l=name2.count("l")
o=name2.count("o")
v=name2.count("v")
e=name2.count("e")

true=str(t+r+u+e)
love=str(l+o+v+e)

print("Your Percentage is "+true+love)