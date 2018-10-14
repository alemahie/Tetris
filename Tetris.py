"""
Projet n°3 : Tetris
"""
__author__ = "Lemahieu Antoine"
__date__ = "25/11/2017"

import turtle, random, time, copy

def grid():
    """
    Interface / Grille.
    """
    interface.up()
    interface.goto(-225,320)
    interface.down()
    for i in range(1,20):
        interface.fd(350)
        interface.up()
        interface.goto(-225,(320-(i*35)))
        interface.down()
    interface.left(90)
    interface.up()
    interface.goto(125,320)
    interface.left(180)
    for j in range(1,12):
        interface.down()
        interface.fd(630)
        interface.up()
        interface.goto((125-(j*35)),320)
    interface.up()
    interface.goto(260,250)             #Score
    interface.write("Score", move=False, align="center",font=("Arial",20,"normal"))
    interface.goto(260,130)             #Lignes
    interface.write("Lines", move=False, align="center",font=("Arial",20,"normal"))
    turtle.update()

def score_init():
    """
    Initialise le score affiché.
    """
    scr.clear()
    scr.up()
    scr.goto(170,240)
    scr.down()
    scr.goto(350,240)
    scr.goto(350,190)
    scr.goto(170,190)
    scr.goto(170,240)
    scr.up()
    scr.goto(260,200)
    scr.write("0", move=False, align="center",font=("Arial",20,"normal"))

def ligne_init():
    """
    Initialise le nombre de lignes affichées.
    """
    line.clear()
    line.up()
    line.goto(170,120)
    line.down()
    line.goto(350,120)
    line.goto(350,70)
    line.goto(170,70)
    line.goto(170,120)
    line.up()
    line.goto(260,80)
    line.write("0", move=False, align="center",font=("Arial",20,"normal"))
    
def matrice():
    """
    Créé la matrice dans laquelle les briques bougent.
    """
    global matrice_tetris
    matrice_tetris = []
    for i in range(21):
        matrice_tetris.append([10])
        for j in range(10):
            (matrice_tetris[i]).append(0)
        matrice_tetris[i].append(10)
    matrice_tetris.append([10,10,10,10,10,10,10,10,10,10,10,10])

def lose_check(lose, fall):
    """
    Vérifie si le joueur a perdu.
    """
    for i in range(1,11):
        if matrice_tetris[3][i] in [3,4,5,6,7,8,9]:
            lose = True
            fall = False
    return lose, fall

def brick_check(fall):
    """
    Vérifie si la brique touche une brique en dessous d'elle et l'arrête.
    """
    for i in range(20,2,-1):
        for j in range(11,0,-1):  
            if matrice_tetris[i][j] == 1 and (matrice_tetris[i+1][j] in [3,4,5,6,7,8,9,10]):
                brick_tracer()
                if brick[-1] == "yellow":
                    matrice_tetris[i][j] = 3
                elif brick[-1] == "#00FFFF":
                    matrice_tetris[i][j] = 4
                elif brick[-1] == "#CC00CC":
                    matrice_tetris[i][j] = 5
                elif brick[-1] == "orange":
                    matrice_tetris[i][j] = 6
                elif brick[-1] == "blue":
                    matrice_tetris[i][j] = 7
                elif brick[-1] == "#38E638":
                    matrice_tetris[i][j] = 8
                elif brick[-1] == "red":
                    matrice_tetris[i][j] = 9 
                global temps
                temps = 0.001
                fall = False
    if fall == False:
        for i in range(20,3,-1):
            for j in range(11,0,-1): 
                if matrice_tetris[i][j] == 1:
                    if brick[-1] == "yellow":
                        matrice_tetris[i][j] = 3
                    elif brick[-1] == "#00FFFF":
                        matrice_tetris[i][j] = 4
                    elif brick[-1] == "#CC00CC":
                        matrice_tetris[i][j] = 5
                    elif brick[-1] == "orange":
                        matrice_tetris[i][j] = 6
                    elif brick[-1] == "blue":
                        matrice_tetris[i][j] = 7
                    elif brick[-1] == "#38E638":
                        matrice_tetris[i][j] = 8
                    elif brick[-1] == "red":
                        matrice_tetris[i][j] = 9 
                elif matrice_tetris[i][j] == 2:
                    matrice_tetris[i][j] = 0
    return fall

def ligne_check(ligne, score):
    """
    Vérifie si une ligne est pleine.
    """
    ligne_provisoire = 0
    for i in range(3,(len(matrice_tetris)-1)):
        j = 10
        while matrice_tetris[i][j] != 0:
            j -= 1
            if j == -1: #Ligne complète   
                matrice_tetris[i] = [10,0,0,0,0,0,0,0,0,0,0,10]
                for k in range(i,3,-1):
                    for l in range(1,11):
                        matrice_tetris[k][l] = matrice_tetris[k-1][l]
                brick_redraw()    
                turtle.update()
                ligne += 1
                ligne_provisoire += 1
                line.up()
                line.clear()
                line.goto(170,120)        #Nombre de lignes
                line.down()
                line.goto(350,120)
                line.goto(350,70)
                line.goto(170,70)
                line.goto(170,120)
                line.up()
                line.goto(260,80)
                line.write(ligne, move=False, align="center",font=("Arial",20,"normal"))
                turtle.update()
    if ligne_provisoire == 1:
        score += 100
    elif ligne_provisoire == 2:
        score += 300
    elif ligne_provisoire == 3:
        score += 1000
    elif ligne_provisoire == 4:
        score += 4000 
    scr.up()
    scr.clear()
    scr.goto(170,240)        #Score
    scr.down()
    scr.goto(350,240)
    scr.goto(350,190)
    scr.goto(170,190)
    scr.goto(170,240)
    scr.up()
    scr.goto(260,200)
    scr.write(score, move=False, align="center",font=("Arial",20,"normal"))
    turtle.update()
    return ligne, score

def reset():
    """
    Réinitialise le jeu pour jouer à nouveau.
    """
    interface.clear()
    interface.left(90)
    grid()
    score_init()
    ligne_init()
    turtle.update()
    game()

def random_brick():
    """
    Créé une brique aléatoirement.
    """
    global brick
    random_number = random.randint(1,7)
    if random_number == 1:      #Carré
        brick = [[1,1],[1,1],"yellow"]
    elif random_number == 2:    #Barre
        brick = [[1,1,1,1],"#00FFFF"]
    elif random_number == 3:    #Croix / T
        brick = [[2,1,2],[1,1,1],"#CC00CC"] 
    elif random_number == 4:    #L normal
        brick = [[2,2,1],[1,1,1],"orange"]  
    elif random_number == 5:    #L inversé
        brick = [[1,2,2],[1,1,1],"blue"]  
    elif random_number == 6:    #S normal _|¨¨
        brick = [[2,1,1],[1,1,2],"#38E638"]
    elif random_number == 7:    #S inversé ¨¨|_
        brick = [[1,1,2],[2,1,1],"red"]
    time.sleep(0.1)

def brick_init(x, y):
    """
    Rajoute la nouvelle brick au jeu.
    """
    for i in range(len(brick)-1):
        for j in range(len(brick[0])):
            matrice_tetris[i+y][5+j+x] = brick[i][j]
    brick_tracer()

def brick_tracer():
    """
    Trace les briques.
    """
    tetro.clear()
    tetro.fillcolor(brick[-1])
    for i in range(3,21):
        for j in range(1,11):
            if matrice_tetris[i][j] == 1:
                tetro.up()
                tetro.goto(((-207+((j-1)*35))-17),((302-((i-3)*35))+17))
                tetro.down()
                tetro.begin_fill()
                tetro.goto(((-207+((j-1)*35))-17),((302-((i-3)*35))-17))
                tetro.goto(((-207+((j-1)*35))+17),((302-((i-3)*35))-17))
                tetro.goto(((-207+((j-1)*35))+17),((302-((i-3)*35))+17))
                tetro.up()
                tetro.end_fill()
    turtle.update()

def brick_fall():
    """
    Fait tomber la brique.
    """
    x = 0
    y = 1
    move(x, y)

def right():
    """
    Bouge la pièce vers la droite.
    """
    x = 1
    y = 0
    move(x, y)
    
def left():
    """
    Bouge la pièce vers la gauche.
    """
    x = -1
    y = 0
    move(x, y)
    
def down():
    """
    Accélère la descente de la pièce.
    """
    global temps, downed
    downed = True
    temps = 0.000000004

def up():
    boucle = 100
    rotate()

def spacebar():
    reset()

def echap():
    turtle.bye()

def rotate():
    """
    Tourne la pièce à 90°
    """
    global brick
    new_brick = []
    for i in range(len(brick[0])):
        new_brick.append([])
        for j in range(len(brick)-1):
            new_brick[i].append(brick[(len(brick)-2)-j][i])
    new_brick.append(brick[-1])
    brick = copy.deepcopy(new_brick)

def brick_redraw():
    """
    Redessine les bricks tombées lorsque la brick a fini de tomber.
    """
    redraw.clear()
    for i in range(2,21):
        for j in range(1,11):
            if matrice_tetris[i][j] == 3:
                redraw.fillcolor("yellow")
            elif matrice_tetris[i][j] == 4:
                redraw.fillcolor("#00FFFF")
            elif matrice_tetris[i][j] == 5:
                redraw.fillcolor("#CC00CC")
            elif matrice_tetris[i][j] == 6:
                redraw.fillcolor("orange")
            elif matrice_tetris[i][j] == 7:
                redraw.fillcolor("blue")
            elif matrice_tetris[i][j] == 8:
                redraw.fillcolor("#38E638")
            elif matrice_tetris[i][j] == 9:
                redraw.fillcolor("red")
            if matrice_tetris[i][j] in [3,4,5,6,7,8,9]:
                redraw.up()
                redraw.goto(((-207+((j-1)*35))-17),((302-((i-3)*35))+17))
                redraw.down()
                redraw.begin_fill()
                redraw.goto(((-207+((j-1)*35))-17),((302-((i-3)*35))-17))
                redraw.goto(((-207+((j-1)*35))+17),((302-((i-3)*35))-17))
                redraw.goto(((-207+((j-1)*35))+17),((302-((i-3)*35))+17))
                redraw.up()
                redraw.end_fill()
    turtle.update()
    
def move(x, y):
    """
    Bouge les pièces en fonction des fonctions qui l'appelle.
    """
    global boucle, downed
    if downed:
        boucle = 1
    else:
        boucle = 100
    
    
    exception = 0
    gauche_check = 0
    for i in range(2,20):
        for j in range(1,11):
            if matrice_tetris[i][j] == 1 or matrice_tetris[i][j] == 2:
                matrice_tetris[i][j] = 0
                bas, droite = i, j
                if gauche_check == 0:
                    gauche_check = j   
    haut = (bas-(len(brick)-2))
    gauche = (droite-(len(brick[0])-1))
    if brick[-1] == "blue" and len(brick) == 4 and brick[1][1] == 2:
        if (matrice_tetris[bas][droite+1] in [3,4,5,6,7,8,9]) and gauche != gauche_check:
            remember1 = matrice_tetris[bas][droite+1]
            remember2 = matrice_tetris[bas+1][droite+1]
            for k in range(len(brick)-1):
                for l in range(len(brick[0])):
                    matrice_tetris[haut+1+k][droite+l] = brick[k][l]
            matrice_tetris[haut+2][droite+1] = remember1
            matrice_tetris[haut+3][droite+1] = remember2
            exception = 1
    if brick[-1] == "orange" and len(brick) == 4 and brick[1][0] == 2:
        if matrice_tetris[bas][gauche] in [3,4,5,6,7,8,9]:
            for k in range(len(brick)-1):
                for l in range(len(brick[0])):
                    if brick[k][l] == 1:
                        matrice_tetris[haut+1+k][gauche+l] = brick[k][l]
            exception = 1
    if exception == 0:
        for i in range(len(brick)-1):
            if matrice_tetris[haut+i][gauche+x] in [3,4,5,6,7,8,9,10] or matrice_tetris[haut+i][droite+x] in [3,4,5,6,7,8,9,10]:
                exception = 1       #Empêche de traverser les blocs sur la gauche ou droite.
        if exception == 0:      
            for k in range(len(brick)-1):
                for l in range(len(brick[0])):
                    remember = matrice_tetris[haut+y+k][gauche+x+l]
                    matrice_tetris[haut+y+k][gauche+x+l] = brick[k][l]
                    if remember != 0:
                        matrice_tetris[haut+y+k][gauche+x+l] = remember
        else:
            for m in range(len(brick)-1):
                for n in range(len(brick[0])):
                    matrice_tetris[haut+m][gauche+n] = brick[m][n]  
    brick_tracer()
    
def game():
    """
    Là ou le jeu se déroule.
    """
    global temps, boucle, downed
    temps = 0.001
    boucle = 100
    downed = False
    ligne = 0
    score = 0
    lose = False
    matrice()
    while lose != True:
        fall = True
        downed = False
        brick_redraw()
        ligne, score = ligne_check(ligne, score)
        random_brick()
        x, y = 0, 2
        brick_init(x, y)
        while fall == True:
            brick_tracer()
            turtle.onkey(up, "Up")
            turtle.onkey(right, "Right")
            turtle.onkey(left, "Left")
            turtle.onkey(down, "Down")
            turtle.listen()
            while fall == True:
                print(boucle)
                time.sleep(temps)
                if temps == 0.000000004:
                    score += 10
                lose, fall = lose_check(lose, fall)
                fall = brick_check(fall)
                lose, fall = lose_check(lose, fall)
                if fall == True and (boucle == 0 or downed):
                    if downed:
                        boucle = 1
                    else:
                        boucle = 100
                    brick_fall()  
                brick_tracer()
                fall = brick_check(fall)
                boucle -= 1
            if fall == True:
                turtle.mainloop()

    interface.up()                 #Le joueur a perdu.
    interface.goto(-220,140)
    interface.down()
    interface.fillcolor("Black")
    interface.begin_fill()
    interface.goto(120,140)
    interface.goto(120,-130)
    interface.goto(-220,-130)
    interface.goto(-220,140)
    interface.end_fill()
    interface.up()
    interface.goto(-50,30)
    interface.write("GAME OVER", move=False, align="center",font=("Arial",35,"normal"))
    interface.goto(-50,-30)
    interface.write("Press :", move=False, align="center",font=("Arial",20,"normal"))
    interface.goto(-50,-70)
    interface.write("'Spacebar' to continue", move=False, align="center",font=("Arial",20,"normal"))
    interface.goto(-50,-110)
    interface.write("'Esc' to exit", move=False, align="center",font=("Arial",20,"normal"))
    turtle.onkeypress(spacebar, "space")
    turtle.onkeypress(echap, "Escape")
    turtle.listen()

if __name__ == "__main__":
    turtle.title("Tetris")
    turtle.bgcolor("Black")
    turtle.tracer(0)
    interface = turtle.Turtle()
    interface.hideturtle()
    interface.color("White")
    tetro = turtle.Turtle()
    tetro.hideturtle()
    tetro.color("White")
    redraw = turtle.Turtle()
    redraw.hideturtle()
    redraw.color("White")
    scr = turtle.Turtle()
    scr.hideturtle()
    scr.color("White")
    line = turtle.Turtle()
    line.hideturtle()
    line.color("White")
    for i in range(13,0,-1):        #Trace le TETRIS d'introduction
        interface.clear()
        interface.up()
        interface.goto(-295,100+(35*i))    #T du Tetris
        interface.down()
        interface.fillcolor("#00FFFF")
        interface.begin_fill()
        interface.goto(-190,100+(35*i))
        interface.goto(-190,65+(35*i))
        interface.goto(-225,65+(35*i))
        interface.goto(-225,-75+(35*i))
        interface.goto(-260,-75+(35*i))
        interface.goto(-260,65+(35*i))
        interface.goto(-295,65+(35*i))
        interface.goto(-295,100+(35*i))
        interface.end_fill()
        interface.up()
        interface.goto(-185,100+(35*i))    #E du Tetris
        interface.down()
        interface.fillcolor("red")
        interface.begin_fill()
        interface.goto(-80,100+(35*i))
        interface.goto(-80,65+(35*i))
        interface.goto(-150,65+(35*i))
        interface.goto(-150,30+(35*i))
        interface.goto(-115,30+(35*i))
        interface.goto(-115,-5+(35*i))
        interface.goto(-150,-5+(35*i))
        interface.goto(-150,-40+(35*i))
        interface.goto(-80,-40+(35*i))
        interface.goto(-80,-75+(35*i))
        interface.goto(-185,-75+(35*i))
        interface.goto(-185,100+(35*i))
        interface.end_fill()
        interface.up()
        interface.goto(-75,100+(35*i))     #T du Tetris
        interface.fillcolor("orange")
        interface.down()
        interface.begin_fill()
        interface.goto(30,100+(35*i))
        interface.goto(30,65+(35*i))
        interface.goto(-5,65+(35*i))
        interface.goto(-5,-75+(35*i))
        interface.goto(-40,-75+(35*i))
        interface.goto(-40,65+(35*i))
        interface.goto(-75,65+(35*i))
        interface.goto(-75,100+(35*i))
        interface.end_fill()
        interface.up()
        interface.goto(35,100+(35*i))      #R du Tetris
        interface.fillcolor("blue")
        interface.down()
        interface.begin_fill()
        interface.goto(140,100+(35*i))
        interface.goto(140,30+(35*i))
        interface.goto(105,30+(35*i))
        interface.goto(105,65+(35*i))
        interface.goto(70,65+(35*i))
        interface.goto(70,30+(35*i))
        interface.goto(105,30+(35*i))
        interface.goto(105,-5+(35*i))
        interface.goto(70,-5+(35*i))
        interface.goto(70,-75+(35*i))
        interface.goto(35,-75+(35*i))
        interface.goto(35,100+(35*i))
        interface.end_fill()
        interface.up()
        interface.goto(105,-5+(35*i))
        interface.down()
        interface.begin_fill()
        interface.goto(140,-5+(35*i))
        interface.goto(140,-75+(35*i))
        interface.goto(105,-75+(35*i))
        interface.goto(105,-5+(35*i))
        interface.end_fill()
        interface.up()
        interface.goto(145,100+(35*i))     #I du Tetris
        interface.fillcolor("#38E638")
        interface.begin_fill()
        interface.down()
        interface.goto(180,100+(35*i))
        interface.goto(180,-75+(35*i))
        interface.goto(145,-75+(35*i))
        interface.goto(145,100+(35*i))
        interface.end_fill()
        interface.up()
        interface.goto(185,100+(35*i))     #S du Tetris
        interface.fillcolor("yellow")
        interface.down()
        interface.begin_fill()
        interface.goto(290,100+(35*i))
        interface.goto(290,65+(35*i))
        interface.goto(220,65+(35*i))
        interface.goto(220,30+(35*i))
        interface.goto(290,30+(35*i))
        interface.goto(290,-75+(35*i))
        interface.goto(185,-75+(35*i))
        interface.goto(185,-40+(35*i))
        interface.goto(255,-40+(35*i))
        interface.goto(255,-5+(35*i))
        interface.goto(185,-5+(35*i))
        interface.goto(185,100+(35*i))
        interface.end_fill()
        turtle.update()
        time.sleep(0.05)
        
    time.sleep(1)
    interface.up()
    interface.goto(0,-130)
    interface.write("Press 'Spacebar' to begin !", move=False, align="center",font=("Arial",20,"normal"))
    interface.goto(0,-210)
    interface.write("Controls", move=False, align="center",font=("Arial",20,"normal"))
    interface.goto(0,-250)
    interface.write("'Up' = Rotate   'Down' = High Speed", move=False, align="center",font=("Arial",20,"normal"))
    interface.goto(0,-290)
    interface.write("'Left' = Left   'Right' = Right", move=False, align="center",font=("Arial",20,"normal"))
    interface.right(90)
    turtle.onkeypress(spacebar, "space")
    turtle.listen()
    turtle.mainloop()
