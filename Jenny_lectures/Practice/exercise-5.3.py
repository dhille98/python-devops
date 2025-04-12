# calucate the BMI value 

weight = float(input("Enter the your weight in kgs:"))
height = float(input("Enter the your Height in meters:"))


bmi = weight/height ** 2

# print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are Under weight ")
elif bmi < 25:
     print(f"Your BMI is {bmi} and you are Under Normal Weight. ")
elif bmi < 30:
     print(f"Your BMI is {bmi} and you are Over weight ")
elif bmi < 35:
     print(f"Your BMI is {bmi} and you are Obese ")
else:
     print(f"Your BMI is {bmi} and you are Clinically Obese. ")
