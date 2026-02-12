from FunctionHelper_SlotMachine import deposit, slot_result, bet_sum, bet_type, money_made

sum_deposit = 0

while True:
    print("Current money in your deposit: %.2f" %sum_deposit)
    user_input = input("What do you want to do? \n(1) Deposit Money \n(2)Play the slot machine \n(Q)Quit\n")
    if user_input == "1":
        sum_deposit = deposit(sum_deposit)
    elif user_input == "2":
        while True:
            print("Welcome to the slot machine!")
            bet_sum_play = bet_sum(sum_deposit)
            sum_deposit -= bet_sum_play
            bet_type_play = bet_type(bet_sum_play)
            print("Money left in deposit:", sum_deposit)
            slot_result_play = slot_result()
            prise = money_made(bet_type_play, bet_sum_play, slot_result_play)
            sum_deposit += prise
            second_user_input = input("Money left in deposit:" + str(sum_deposit) +"\nif you wish to quit the slot machine, press (Q). If you wish to continue, press Enter.\n")
            if second_user_input.lower() == "q":
                break
    elif user_input.lower() == 'q':
        print("Have a nice day")
        break
    else:
        print("Invalid input. Please try again.")
