import random

x = "y"

while x  == "y":
    no = random.randint(1,6)

    if no ==1:
        print(" _____")
        print("|     |")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("|_____|")
    if no ==2:
        print(" _____")
        print("|     |")
        print("|     |")
        print("| 0 0 |")
        print("|     |")
        print("|_____|")
    if no ==3:
        print(" _____")
        print("|     |")
        print("|  o  |")
        print("|  o  |")
        print("|  o  |")
        print("|_____|")
    if no ==4:
        print(" _____")
        print("|     |")
        print("| o o |")
        print("|     |")
        print("| o o |")
        print("|_____|")
    if no ==5:
        print(" _____")
        print("|     |")
        print("| o o |")
        print("|  0  |")
        print("| o o |")
        print("|_____|")
    if no ==6:
        print(" _____")
        print("|     |")
        print("| ooo |")
        print("| ooo |")
        print("|_____|")
    x = input("Enter y to roll again and e to exit.")
    print("\n")
