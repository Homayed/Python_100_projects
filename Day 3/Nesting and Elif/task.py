print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Whats your age?"))
    if age < 12:
        print("You pay 5$")
    elif age <= 18:
        print("You pay 7$")
    else:
        print("You pay 12$")
else:
    print("Sorry you have to grow taller before you can ride.")

weight2 = int(input("Weight"))
height2 = float(input("Height"))

bmi = weight2 / (height2 ** 2)

if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("normal weight")
else:
    print("overweight")
