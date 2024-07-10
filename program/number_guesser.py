import random
import math

def get_total_chances(level, upper, lower):
    """
    This calculates the total chances a player gets depending on their difficulty level
    Range size is set by the player: upper bound = highest number and lower bound = lowest number
    """
    range_size = upper - lower + 1
    if level == 1:
        return math.ceil(math.log(range_size, 2)) + 3  # Easy: more chances
    elif level == 2:
        return math.ceil(math.log(range_size, 2))  # Medium: normal chances
    elif level == 3:
        return math.ceil(math.log(range_size, 2)) - 2  # Hard: fewer chances

def number_guesser_game():
    """
    Main Function of the game
    """
    print("Choose a level: 1 (Easy), 2 (Medium), 3 (Hard)")
    level = int(input("Enter the level:- "))
    if level not in [1, 2, 3]:
        print("Invalid level. Please choose 1, 2, or 3.")
        return

    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))

    x = random.randint(lower, upper)   # Generates random number between player's range
    total_chances = get_total_chances(level, upper, lower)  # Total chances based off player's chosen level
    print("\n\tYou've only", total_chances, "chances to guess the integer!\n")

    count = 0
    flag = False  # Checks if number is guessed

    while count < total_chances:
        count += 1
        guess = int(input("Guess a number:- "))
# Player won1
        if x == guess:
            print("Congratulations! You did it in", count, "tries.")
            flag = True
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You guessed too high!")
# Player lost
    if not flag:
        print("\nThe number was %d" % x)
        print("\tBetter luck next time!")

if __name__ == "__main__":
    number_guesser_game()
