import random

points = 0

def gierka():


    computer_choice = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
    x = input('Type: Rock, Paper, Scissor, Lizard, Spock\n')

    if x == random.choice(computer_choice):
        print('Ok. The number of points equals ' + str( points + 1 ))
    else:
        print('Wrong. The number of points equals ' + str(points))

    x = input('Type: Rock, Paper, Scissor, Lizard, Spock\n')
    if x == random.choice(computer_choice):
        print('Ok. The number of points equals ' + str(points + 1))
    else:
        print('Wrong. The number of points equals ' + str(points))

    x = input('Type: Rock, Paper, Scissor, Lizard, Spock\n')
    if x == random.choice(computer_choice):
        print('Ok. The number of points equals ' + str(points +1))
    else:
        print('Wrong. The number of points equals ' + str(points))

    if points == 3:
        print("You won, Congratulations!")
    elif points > 0:
        print("You lost by " + str(3 - points) + ' points')
    elif points == 0:
        print( "You lost by 3 points")

    finish = input("Try again? yes or no\n")
    while finish == "yes":
        gierka()
    else:
        print("Thanks for playing")

gierka()

