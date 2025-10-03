import turtle
turtle.setup(width=800, height=800)  # Iestatām loga izmērus
turtle.speed(10)  # Iestatām maksimāli ātru zīmēšanas ātrumu
# kegela funkcija zīmē taisnstūri (ķieģeli)
def draw_brick(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
def draw_half_brick(width, height):
    for _ in range(2):
        
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width / 2)
        turtle.left(90)
# sienas zīmēšanas funkcija
def draw_wall(rows, columns, brick_width, brick_height):
    # Sākotnējā pozīcija sienas zīmēšanai
    start_x, start_y = -400, -150
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()

    # Rindas ķieģeļu zīmēšana
    for row in range(rows):
        for col in range(columns):
            if row % 2 != 0:  # Pāra rindas
                if col == 0:
                    draw_half_brick(brick_width, brick_height)
                else:
                    draw_brick(brick_width, brick_height)
                turtle.penup()
                turtle.forward(brick_width)
                turtle.pendown()
                if col == columns - 1:  # Ja ir pēdējais ķieģelis, zīmējam pusi
                    draw_half_brick(brick_width, brick_height)
            else:  # Nepāra rindas (novedam ķieģeļus uz pusēm)
                if col == 0:  # Sadzīvojam pirmo ķieģeli uz pusi
                    turtle.penup()
                    turtle.forward(brick_width / 2)
                    turtle.pendown()
                draw_brick(brick_width, brick_height)
                

                turtle.penup()
                turtle.forward(brick_width)
                turtle.pendown()
        # Pārejam uz jauno rindu
        turtle.penup()
        turtle.goto(start_x, start_y + (brick_height * (row + 1)))
        turtle.pendown()

# Galvenais kods
def main():
    turtle.speed(0)  # Iestatām maksimāli ātru zīmēšanas ātrumu

    # Iegūstam parametrus no lietotāja
    rows = int(input("Ievadiet rindu skaitu: "))
    columns = int(input("Ievadiet kolonnu skaitu: "))
    brick_width = int(input("Ievadiet ķieģeļa platumu: "))
    brick_height = int(input("Ievadiet ķieģeļa augstumu: "))

    # Zīmējam ķieģeļu sienu
    draw_wall(rows, columns, brick_width, brick_height)

    # Pabeidzam zīmēšanu
    turtle.done()

if __name__ == "__main__":
    main()