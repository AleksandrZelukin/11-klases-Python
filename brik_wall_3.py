import matplotlib.pyplot as plt
import matplotlib.patches as patches

def zimet_sienu(rindas=12, kolonnas=14,
                kiegela_platums=1.0, kiegela_augstums=0.5,
                suve=0.03,
                kiegela_krasa="#b22222", suves_krasa="#f2f2f2"):
    """
    Zīmē ķieģeļu sienu ar norādītajiem parametriem.
    
    rindas          – rindu skaits
    kolonnas        – veselo ķieģeļu skaits pāra rindā
    kiegela_platums – ķieģeļa platums
    kiegela_augstums– ķieģeļa augstums
    suve            – šuves biezums
    kiegela_krasa   – ķieģeļa krāsa (piemēram, '#b22222')
    suves_krasa     – šuvju/fona krāsa (piemēram, '#f2f2f2')
    """
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_facecolor(suves_krasa)  # fons – java starp ķieģeļiem

    for r in range(rindas):
        y = r * (kiegela_augstums + suve)

        if r % 2 == 0:  
            # pāra rinda: tikai veseli ķieģeļi
            x_sakums = 0.0
            kiegeli_rinda = kolonnas
            nobide = 0
        else:
            # nepāra rinda: puse ķieģeļa kreisajā un labajā pusē
            x_sakums = 0.0
            kiegeli_rinda = kolonnas - 1
            nobide = 0.5

            # kreisā puse
            rect = patches.Rectangle(
                (x_sakums, y), kiegela_platums/2, kiegela_augstums,
                facecolor=kiegela_krasa, edgecolor="black", linewidth=1
            )
            ax.add_patch(rect)

        # galvenie ķieģeļi
        for c in range(kiegeli_rinda):
            x = x_sakums + nobide*kiegela_platums + nobide*suve + c * (kiegela_platums + suve)
            rect = patches.Rectangle(
                (x, y), kiegela_platums, kiegela_augstums,
                facecolor=kiegela_krasa, edgecolor="black", linewidth=1
            )
            ax.add_patch(rect)

        if r % 2 == 1:
            # labā puse
            x = x_sakums + nobide*kiegela_platums + nobide*suve + kiegeli_rinda * (kiegela_platums + suve)
            rect = patches.Rectangle(
                (x, y), kiegela_platums/2, kiegela_augstums,
                facecolor=kiegela_krasa, edgecolor="black", linewidth=1
            )
            ax.add_patch(rect)

    # Noformējums
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.show()


# Piemērs: zīmē sienu ar noklusētajiem parametriem
zimet_sienu()

# Piemērs: mazāka siena ar gaišākiem ķieģeļiem
# zimet_sienu(rindas=6, kolonnas=8, kiegela_krasa="#ff6347", suves_krasa="#ffffff")
