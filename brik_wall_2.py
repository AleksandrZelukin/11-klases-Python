import turtle
import time

def zimet_sienu_turtle(rindas=8, kolonnas=10,
                       kiegela_platums=60, kiegela_augstums=30,
                       suve=2,
                       kiegela_krasa="firebrick", suves_krasa="lightgray",
                       animacija=True, atrums=0.05,
                       no_apaksas=True):
    """
    Zīmē ķieģeļu sienu ar 'turtle' bibliotēku.
    Var animēt sienas veidošanu, sākot no apakšas vai no augšas.
    
    rindas – cik rindu zīmēt
    kolonnas – veselo ķieģeļu skaits pāra rindā
    kiegela_platums / kiegela_augstums – izmēri
    suve – šuves biezums
    animacija – True/False, vai rādīt animāciju
    atrums – pauze starp ķieģeļiem sekundēs
    no_apaksas – True, ja animācija sākas no apakšas
    """

    # Aprēķinām sienas platumu un augstumu
    platums = kolonnas * (kiegela_platums + suve)
    augstums = rindas * (kiegela_augstums + suve)

    # Logs un bruņurupucis
    ekrans = turtle.Screen()
    ekrans.bgcolor(suves_krasa)
    ekrans.setup(width=platums + 100, height=augstums + 100)
    ekrans.title("Ķieģeļu siena")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(1)

    def zimet_kiegelis(x, y, platums, augstums):
        """Zīmē vienu ķieģeli no punkta (x,y)"""
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(kiegela_krasa)
        t.begin_fill()
        for _ in range(2):
            t.forward(platums)
            t.left(90)
            t.forward(augstums)
            t.left(90)
        t.end_fill()
        if animacija:
            time.sleep(atrums)

    # Sākuma punkts (augšējais kreisais stūris)
    start_x = -platums / 2
    start_y = augstums / 2

    # Ja no apakšas – mainām rindu secību
    rindas_seciba = range(rindas-1, -1, -1) if no_apaksas else range(rindas)

    # Sienas zīmēšana
    for r in rindas_seciba:
        y = start_y - r * (kiegela_augstums + suve)

        if r % 2 == 0:
            # pāra rinda: tikai veseli ķieģeļi
            x_start = start_x
            kiegeli_rinda = kolonnas
            nobide = 0
        else:
            # nepāra rinda: puse ķieģeļa kreisajā un labajā pusē
            x_start = start_x
            kiegeli_rinda = kolonnas - 1
            nobide = 0.5
            # kreisā puse
            zimet_kiegelis(x_start, y, kiegela_platums/2-suve, kiegela_augstums)

        # galvenie ķieģeļi
        for c in range(kiegeli_rinda):
            x = x_start + nobide*kiegela_platums + c * (kiegela_platums + suve)
            zimet_kiegelis(x, y, kiegela_platums, kiegela_augstums)

        if r % 2 == 1:
            # labā puse
            x = x_start + nobide*kiegela_platums + kiegeli_rinda * (kiegela_platums + suve)
            zimet_kiegelis(x, y, kiegela_platums/2, kiegela_augstums)

    turtle.done()


# Piemērs: animācija no apakšas (kā īsta siena)
zimet_sienu_turtle(rindas=16, kolonnas=12, kiegela_platums=50, kiegela_augstums=25,
                   suve=4, animacija=True, atrums=0.1, no_apaksas=True)
