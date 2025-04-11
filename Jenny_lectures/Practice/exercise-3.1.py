# calculate BMI 
# weight / ( height * height)

Height = float(input("Enter the Persion Hegiht in meters:"))
Weight = float(input("Enter the Weight of persion in kgs:"))

sq_Height = (Height * Height) 

Bmi_Value = (Weight / sq_Height)

print(float(Bmi_Value)) 