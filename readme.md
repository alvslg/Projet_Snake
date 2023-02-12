from tkinter import * 

def right(event):
    # Se déplacer vers la droite
    global perso_x2
    global perso_x
    perso_x +=25
    perso_x2 +=25
   

def left(event):
    # Se déplacer vers la gauche
    global perso_x2
    global perso_x
    perso_x -=25
    perso_x2 -=25

    
def down(event):
    # Se déplacer vers le bas
    global perso_y2
    global perso_y
    perso_y +=25
    perso_y2 +=25
  
def up(event):
    # Se déplacer vers le haut
    global perso_y2
    global perso_y
    perso_y -=25
    perso_y2 -=25

def moteur():
    #Rafraichissement de la fenêtre
    global direction
    dessine_laby()
    dessine_perso()
    fenetre.after(50, moteur)

def dessine_perso():
    #Dessine le personnage qu'on controlera (un carré en gros)
    global perso_x
    global perso_y
    print(perso_x, perso_y)
    perso = canvas.create_rectangle(perso_x,perso_y,perso_x2,perso_y2,fill="black")

def dessine_laby():
    #Dessine un labyrinthe grâce à la liste de liste
    OFFSET_X = 150
    OFFSET_Y = 125
    ECH = 50
    for y in range(len(murs_h)):
        for x in range(len(murs_v[y])):
            if murs_h[y][x] == 1:
                canvas.create_line(x*ECH+OFFSET_X, y*ECH+OFFSET_Y, x*ECH+ECH+OFFSET_X, y*ECH+OFFSET_Y)                      
    for y in range(len(murs_v)):
        for x in range(len(murs_h[x])):
            if murs_v[y][x] == 1:
                canvas.create_line(x*ECH+OFFSET_X, y*ECH+OFFSET_Y, x*ECH+OFFSET_X, y*ECH+OFFSET_Y+ECH)
    
#Contenu de la fenêtre de jeu
fenetre = Tk()

canvas = Canvas(fenetre, width=600, height=480, background='white')

#Création des bordures du labyrinthe
ligne1 = canvas.create_line(150, 125, 150, 400)
ligne2 = canvas.create_line(200, 125, 450, 125)
ligne3 = canvas.create_line(450, 425, 450, 175)
ligne4 = canvas.create_line(150, 425, 450, 425)

#Titre labyrinthe
txt = canvas.create_text(300, 20, text="Labyrinthe", font="Arial 24 italic", fill="black")

#Structure du labyrinthe
murs_h = [ [0,1,1,0,1,0],
           [0,0,0,0,0,0],
           [1,0,1,0,0,0],
           [0,0,0,1,0,1],
           [0,0,1,1,0,0],
           [0,1,1,0,0,0] ]

murs_v =[ [0,1,1,0,0,1],
          [0,0,1,1,1,1],
          [0,0,1,0,1,0],
          [0,1,0,1,0,1],
          [0,1,0,0,1,1],
          [1,0,0,1,1,0] ]

#Taille, position du personnage
pos_perso =[0, 0]
perso_x = 30
perso_y = 30
perso_x2 = 20
perso_y2 = 20


dessine_laby()
moteur()
canvas.pack()


#Configuration des touches de déplacements
fenetre.bind('<d>', right) 
fenetre.bind('<q>', left) 
fenetre.bind('<s>', down) 
fenetre.bind('<z>', up)

fenetre.mainloop()      
