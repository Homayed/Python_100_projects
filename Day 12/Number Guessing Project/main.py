
import random
import art






def compare(number):
    if computer_number > number:
        print("Too low")
    if computer_number == number:
        return 0
    if computer_number < number:
        print("Too High")


def play():
    is_guessing = False
    is_playing = 10
    print(art.logo)
    print("Guess a number between 1 to 100")
    global computer_number
    computer_number = random.randint(1,100)
    difficulty = input('Which difficulty you want to play in? type to choose "hard" or "easy"\n')
    if difficulty == "easy":
        print("You have a total of 10 chance")
        while is_playing > 0 and not is_guessing:
            playing_number = int(input("Guess a Number"))
            print(f"You Guessed {playing_number}")
            guess_right = compare(playing_number)
            if guess_right == 0:
                print("Congratulations. You Guessed it right")
                is_guessing = True
            else:
                is_playing -= 1
                print(f"You have {is_playing} chance left")
                if is_playing == 0:
                    print("Game Ends")
                    is_guessing = True
    if difficulty == "hard":
        while is_playing > 0 and not is_guessing:
            playing_number = int(input("Guess a Number"))
            print(f"You Guessed {playing_number}")
            guess_right = compare(playing_number)
            if guess_right == 0:
                print("Congratulations. You Guessed it right")
                is_guessing = True
            else:
                is_playing -= 1
                print(f"You have {is_playing-5} chance left")
                if is_playing == 5:
                    print("Game Ends")
                    is_guessing = True

def guess_the_number():
    while input("Do you want to play a game of Guess_The_Number? Press Y/N to start or exit") == "Y":
        print("\n"*20)
        play()

guess_the_number()