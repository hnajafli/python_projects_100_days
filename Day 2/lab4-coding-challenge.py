# The BMI calculator - Body Mass Index

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height = float(height)
weight = int(weight)

bmi = weight / height ** 2

# or

# bmi = weight / (height * height)

print(int(bmi))