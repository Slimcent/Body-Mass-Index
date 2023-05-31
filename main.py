height = float(input("Enter your height in meters"))

weight = float(input("Enter your weight in kg"))

bmi = round((weight / height ** 2), 2)

if bmi < 18.5:
    print(f"Your Bmi is {bmi} and you are Underage")
elif 18.5 < bmi <= 24.9:
    print(f"Your Bmi is {bmi} and you are Normal")
elif 25 < bmi <= 29.29:
    print(f"Your Bmi is {bmi} and you are Overage")
else:
    print(f"Your Bmi is {bmi} and you are Obese")
