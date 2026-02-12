import random
import time

def roll():
    value = random.randint(1,6)
    return value

while True:
    players = input("\nNumber of players (2-10): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 10:
            break
    print("Invalid input.", end="")

round = 1
players_points = []
for i in range(players):
    players_points.append(0)

while True:
    points_max = input("Points goal: ")
    if points_max.isdigit():
        points_max = int(points_max)
        break
    print("Invalid input.", end="")

while max(players_points) < points_max:
    print("Round", round)
    for i in range(players):
        while True:
            choice = input("Player %d, what action do you wish to proceed with?\n(1) Roll ; (2) End Turn\t\t[Current score: %d]\n" %(i+1, players_points[i]))
            if choice == "1":
                print("Rolling...", end="")
                for _ in range(2):
                    time.sleep(0.6)
                    print(".", end="")
                value = roll()
                if value == 1:
                    print("Dice result: 1. \nPoints reset to 0.\n")
                    players_points[i] = 0
                    time.sleep(1.5)
                    break
                else:
                    print("Dice result: %d" %value)
                    players_points[i] += value
                    print("Current points: %d pts.\n" %players_points[i])
                    time.sleep(1.5)
                    if players_points[i] >= points_max:
                        print("Player %d has made it onto the winning side. If nobody else gets to the points goal this round, they'll win the game!\n"%(i+1))
                        time.sleep(2)
                        break

            elif choice == "2":
                print("\nEnd of Turn\n")
                time.sleep(2)
                break
            else:
                print("Invalid Input.")
    print("End of Round", round, "\n")
    round += 1

    for j in range(players):
        print("Player %d: %d pts." %(j+1, players_points[j]))

max_points = max(players_points)
final_winner = []
for k in range(len(players_points)):
    if players_points[k] == max_points:
        final_winner.append(k)
print("With a score of %d, the winner(s) is(are)..." %max_points)
for l in final_winner:
    print("Player %d" %(l+1))
print("\nWell played!")
