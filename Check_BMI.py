# Ask the user to add his height in cm
Height = float(input("Write your height in centimeters : "))
# Ask the user to add his weight in cm
Weight = float(input("Write your weight in Kg : "))
# Apply the equation on BMI
BMI = (Weight/Height/Height)* 10000

#Check that the BMI is more than zero
if BMI > 0 :
# classify the user according to the weight and print a message.
  if BMI < 18.5:
    print("You are underweight")
  elif BMI >= 18.5 and BMI < 25:
    print(f" Your BMI is {BMI} so You ar normal")
  elif BMI >= 25 and BMI <30:
    print(f"Your BMI is {BMI} so You are over weight")
  elif BMI >= 30 and BMI< 35:
    print(f"Your BMI is {BMI} so You are obese")
  else:
    print(f"Your BMI is {BMI} so You are extermely obese")
else:
    print("Enter valid data")





