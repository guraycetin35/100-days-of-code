# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi= weight/height**2
bmi=round(bmi)

if bmi<=18:
  print("Your BMI is 18, you are underweight.")
elif bmi<=22:
  print("Your BMI is 22, you have a normal weight.")
elif bmi<=28:
  print("Your BMI is 28, you are slightly overweight.")
elif bmi<=32:
  print("Your BMI is 22, you have a normal weight.")
elif bmi<=40:
  print("Your BMI is 22, you have a normal weight.") 
  




