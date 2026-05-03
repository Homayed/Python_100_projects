try:
    age = int(input("How old are you?"))
except ValueError:
    print("You need to type an integer as you typed a wrong type of variable")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
