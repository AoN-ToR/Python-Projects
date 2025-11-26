import random
import time

def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def deposit(sum_deposit):
    while True:
        user_deposit = input("How much do you want to deposit? Press (Q) to quit $")
        if isfloat(user_deposit):
            user_deposit = round(float(user_deposit), 2)
            sum_deposit += user_deposit
        elif user_deposit.lower() == "q":
            print("End of deposit.")
            break
        else:
            print("Invalid input.")
        print("Current sum of money deposited: $" + str(sum_deposit))

    return sum_deposit



def slot_result():
    # The chosen model of a slot machine will have 3 weels, and 6 distinct symbols.
    # A win will be defined as having 2 or 3 same symbol in one go.
    # For the sake of this project, we'll use capital letters as the symbols.

    # action of rolling:
    slot_result = []
    for i in range(3):
        time.sleep(1)
        slot_result.append(chr(65 + random.randint(0,5)))
        print(slot_result[i])
    return slot_result



def bet_sum(sum_deposit):
    print("Bet options: \n 10 to 24 -> low reward \n 25 to 69 -> medium reward \n 70 and above -> high reward \nCurrent money deposited: %.2f" %sum_deposit)
    while True:
        bet_sum = input("How much do you want to bet ? (Press (Q) to quit): \n$")
        if isfloat(bet_sum):
            bet_sum = round(float(bet_sum), 2)
            if bet_sum > sum_deposit:
                print("Sum above current sum of money in your deposit")
            elif bet_sum < 10:
                print("Bet sum is too low.")
            else:
                return bet_sum
        elif bet_sum.lower() == "q":
            return "quit"
        else:
            print("Invalid input. Please try again.")

def bet_type(bet_sum):
    if 10 <= bet_sum <= 24:
        print("Select bet type: low. Money injected: %.2f" %bet_sum)
        return "l"
    elif 25 <= bet_sum <= 69:
        print("Select bet type: medium. Money injected: %.2f" %bet_sum)
        return "m"
    elif bet_sum >= 70:
        print("Select bet type: low. Money injected: %.2f" %bet_sum)
        return "h"


def money_made(bet_type, bet_sum, slot_result):

    #low bet roll
    if bet_type == "l":
        if slot_result[0] == slot_result[1] == slot_result[2]:
            print("Jackpot!!")
            prise = round(eval("(1.4 + 0." + str(ord(slot_result[0]) - 65) + ") * " +str(bet_sum)), 2)
            print("Money made:", prise)
            return prise

        elif slot_result[0] == slot_result[1] or slot_result[0] == slot_result[2]:
            print("Got two out of three, congrats!")
            prise = round(eval("1." + str(ord(slot_result[0]) - 65) + " * " +str(bet_sum)), 2)
            print("Money made:", prise)
            return prise
        
        elif slot_result[1] == slot_result[2]:
            print("Got two out of three, congrats!")
            prise = round(eval("1." + str(ord(slot_result[1]) - 65) + " * " +str(bet_sum)), 2)
            print("Money made:", prise)
            return prise

        else:
            print("No matching symbol... better luck net time!")
            prise = 0
            print("(No money made)")
            return prise

    # medium bet roll
    elif bet_type == "m":
        if slot_result[0] == slot_result[1] == slot_result[2]:
            print("Jackpot!!")
            prise = round(eval("2." + str(ord(slot_result[0]) - 65) + " * " +str(bet_sum)), 2)
            print("Money made:", prise)
            return prise

        elif slot_result[0] == slot_result[1] or slot_result[0] == slot_result[2]:
            print("Got two out of three, congrats!")
            prise = round(eval("(1.4 + 0." + str(ord(slot_result[0]) - 65) + ") * " +str(bet_sum)), 2)
            print("Money made:", prise)
            return prise
        
        elif slot_result[1] == slot_result[2]:
            print("Got two out of three, congrats!")
            prise = round(eval("(1.4 + 0." + str(ord(slot_result[1]) - 65) + ") * " +str(bet_sum)), 2)
            print("Money made:", prise)
            return prise

        else:
            print("No matching symbol... better luck net time!")
            prise = 0
            print("(No money made)")
            return prise

    # high bet roll
    elif bet_type == "h":
        if slot_result[0] == slot_result[1] == slot_result[2]:
            print("Jackpot!!")
            prise = round(eval("(2.5 + 0." + str(ord(slot_result[0]) - 65) + ") * " +str(bet_sum)), 2)
            print("Money made:", prise)
            return prise

        elif slot_result[0] == slot_result[1] or slot_result[0] == slot_result[2]:
            print("Got two out of three, congrats!")
            prise = round(eval("2." + str(ord(slot_result[0]) - 65) + " * " +str(bet_sum)), 2)
            print("Money made:", prise)
            return prise
        
        elif slot_result[1] == slot_result[2]:
            print("Got two out of three, congrats!")
            prise = round(eval("2." + str(ord(slot_result[1]) - 65) + " * " +str(bet_sum)), 2)
            print("Money made:", prise)
            return prise

        else:
            print("No matching symbol... better luck net time!")
            prise = 0
            print("(No money made)")
            return prise