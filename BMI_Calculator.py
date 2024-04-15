#BMI Calculator
weight = int(input("Enter your weight in kgs: "))
height = int(input("Enter your height in cms: "))
bmi = round(weight / (height / 100) ** 2, 2)

if bmi <= 18.4:
    remark = "Underweight"
elif bmi <= 24.9:
    remark = "Normal"
elif bmi <= 39.9:
    remark = "Overweight"
else:
    remark = "Obese"

print(f"Your BMI is {bmi} and you fall under {remark} category.")
