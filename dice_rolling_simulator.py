from random import randint
MIN_VALUE = 1
MAX_VALUE = 6

def print_choices():
    print("\nChoose: ")
    print("1 - roll the dice")
    print("2 - exit the game")

def grab_and_print_random_number():
    random_dice_value = randint(MIN_VALUE, MAX_VALUE)
    print(f"\n*Rolled out number is %s*" % random_dice_value)
    
if __name__ == "__main__":

    print("\n***WELCOME TO THE DICE ROLLING SIMULATOR!***")
    while True:
        print_choices()
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            grab_and_print_random_number()
            continue

        elif choice == 2:
            print("\nThanks for using my program! I hope to see next time.")
            break

