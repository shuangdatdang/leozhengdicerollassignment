import random
# random.randrange(1, 7)


def once():
    num1 = random.randrange(1, 7)
    num2 = random.randrange(1, 7)
    ans = num1 + num2
    print(str(num1) + "," + str(num2) + " (sum: " + str(ans) + ")")


def fivetimes():
    p = 1
    while p <= 5:
        once()
        p += 1


def snakey():
    loopy = True
    tries = 0
    while loopy:
        num1 = random.randrange(1, 7)
        num2 = random.randrange(1, 7)
        ans = num1 + num2
        print(str(num1) + "," + str(num2) + " (sum: " + str(ans) + ")")
        if num1 == num2:
            tries += 1
            loopy = False
            print("SNAKE EYES! It took " + str(tries) + " rolls to get snake eyes.")
        elif num1 != num2:
            tries += 1



loop = True
while loop:
    print("Dice Roll Simulator")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times")
    print("4. Roll Dice until Snake Eyes")
    print("5. Exit")
    selection = input("Select an option (1-5): ")
    if selection == "1":
        once()
    elif selection == "2":
        fivetimes()
    elif selection == "3":
        n = input("How many rolls would your like? ")
        m = 1
        while m <= int(n):
            once()
            m += 1
    elif selection == "4":
        snakey()
    elif selection == "5":
        print("Au Revoir")
        loop = False
