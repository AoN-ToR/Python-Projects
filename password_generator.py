import random
import string
import time

char_allowed = []


while True:
    n = input("How many char would you like in your password (q to quit, min length = 3)? ")
    if n.lower == "q":
        quit()
    elif n.isdigit():
        length = int(n)
        if length > 2:
            break
        print("Insufficient length. Try again.")
    else:
        print("Invalid input. Try again.")

while True:
    n = input("Should we use letters in your password? (Y/n) ").lower()
    if n == "y":
        char_allowed.append(True)
        break
    elif n == "n":
        char_allowed.append(False)
        break
    else:
        print("Invalid input. Try again.")

while True:
    n = input("Should we use numbers in your password? (Y/n) ").lower()
    if n == "y":
        char_allowed.append(True)
        break
    elif n == "n":
        char_allowed.append(False)
        break
    else:
        print("Invalid input. Try again.")

while True:
    n = input("Should we use special caracters in your password? (Y/n) ").lower()
    if n == "y":
        char_allowed.append(True)
        break
    elif n == "n":
        char_allowed.append(False)
        break
    else:
        print("Invalid input. Try again.")



def generate(length, char_allowed):
    letters = string.ascii_letters
    numbers = string.digits
    spe_chars = string.punctuation
    password = ""

    list = [letters, numbers, spe_chars]

    list2 = ""

    for i in range(len(list)):
        if char_allowed[i] == True:
            list2 += list[i]
            password = str(password) + str(list[i][random.randint(0, len(list[i])-1)])
            length -= 1
    if len(list2) < 1:
        print("Insufficient material.")
        quit()

    else:
        for i in range(length):
            char = list2[random.randint(0, len(list2)-1)]
            password = str(password) + str(char)

        print(f"\n\nHere is your freshly done new password:\n{password}\n\nSee you later! ")

generate(length, char_allowed)
