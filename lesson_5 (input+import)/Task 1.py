import random
random_number=random.randint(1,10)
entered_value=input("Guess a number between 1 to 10: ")
if not entered_value.isdigit():
    print("Entered value is in incorrect format")
    exit()
else:
    quiz=int(entered_value)
    if quiz==random_number:
        print("WOW! You've done it!")
    else:
        print("It's so sad! The number was", random_number, ". Try again! and don't give up !")

