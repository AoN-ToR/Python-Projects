import random
import turtle


WIDTH, HEIGHT = 700, 600
COLORS = ['blue', 'green', 'yellow', 'orange', 'red', 'cyan', 'violet', 'brown', 'black', 'purple']

def nb_racers():
    while True:
        nb = input("Enter the number of racers (2-10): ")
        if nb.isdigit():
            nb = int(nb)
            if 2 <= nb <= 10:
                return nb
            else:
                print("Invalid input, integer not within accepted range.")
        else:
            print("Invalid input, must enter an integer.")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        j = 0
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[j]
            j += 1

def init_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles



racers = nb_racers()
init_screen()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle of color: ", winner)
