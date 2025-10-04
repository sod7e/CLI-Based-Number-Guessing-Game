import random

print("Let's play a guessing game! I choose a number, and you will try to guess it.")

def main():
    level = input("Select the game difficulty:\n 1. Easy\n 2. Medium\n 3. Hard\n")
    maxNum = 0
    if int(level) == 1:
        maxNum = 20
        continue_game(maxNum)
    elif int(level) == 2:
        maxNum = 50
        continue_game(maxNum)
    elif int(level) == 3:
        maxNum = 100
        continue_game(maxNum)
    else: 
        print("Please enter a valid number!")

def continue_game(maxNum):
    botNum = random.randint(1, maxNum)
    userNum = input(f"Alright, let's go! I've already thought of a number between 1 and {maxNum}, try to guess it.\n") 
    counter = 1
    while int(botNum) != int(userNum):
        if int(userNum) < int(botNum): 
            userNum = input("The number I thought of is higher than " + userNum + ". Try again!\n")
        else:
            userNum = input("The number I thought of is lower than " + userNum + ". Try again!\n")
        
        counter += 1
    print("Congratulations! The number I thought of was", botNum, ", and you guessed it in", counter, "attempts.")

    while True:
        repeat = input("Do you want to play another round? (y/n)")
        if repeat == "y":
            bonus_round()
            break
        elif repeat == "n":
            print("Alright, thanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'!")

def bonus_round():
    print("Let's play another round!")
    main()


if __name__ == "__main__":
    main()