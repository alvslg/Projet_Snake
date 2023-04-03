from tkinter import * 

def right(event):
    """ Se déplacer vers la droite
    """
    global perso_x
    perso_x +=25
    
    
def left(event):
    """ Se déplacer vers la gauche
    """
    global perso_x
    perso_x -=25
     
    
def down(event):
    """ Se déplacer vers le bas
    """
    global perso_y
    if i 
    perso_y +=25

def up(event):
    """ Se déplacer vers le haut
    """
    global perso_y
    perso_y -=25

def moteur():
    """ Rafraichissement de la fenêtre
    """
    global direction
    canvas.delete('all')
    dessine_laby()
    dessine_perso()
    #Création des bordures du labyrinthe
    ligne1 = canvas.create_line(150, 125, 150, 400)
    ligne2 = canvas.create_line(200, 125, 450, 125)
    ligne3 = canvas.create_line(450, 425, 450, 175)
    ligne4 = canvas.create_line(150, 425, 450, 425)
    #Titre labyrinthe
    txt = canvas.create_text(300, 20, text="Labyrinthe", font="Arial 24 italic", fill="black")
    fenetre.after(50, moteur)
   

def dessine_perso():
    """ Dessine le personnage qu'on controlera (un carré en gros)
    """
    global perso_x
    global perso_y
    i = round(perso_x/50 - 18/5)
    j = round(perso_y/50 - 13/5)
    print(perso_x, perso_y, i, j)
    perso = canvas.create_rectangle(perso_x,perso_y,perso_x-10,perso_y-10,fill="black")

def dessine_laby():
    """ Dessine un labyrinthe grâce à la liste de liste
    """
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
    
# Contenu de la fenêtre de jeu

fenetre = Tk()
canvas = Canvas(fenetre, width=1200, height=1200, background='white')

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

# Taille, position du personnage
perso_x = 30
perso_y = 30



dessine_laby()
moteur()
canvas.pack()


# Configuration des touches de déplacements
fenetre.bind('<d>', right) 
fenetre.bind('<q>', left) 
fenetre.bind('<s>', down) 
fenetre.bind('<z>', up)

fenetre.mainloop()








# -*- coding: utf-8 -*-
"""
Programme Snake

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 
from tkinter import font as tkfont
from random import *

def computeNextFrame(numFrame, coordonnee):
    #Affiche le numéro de la frame
    numFrame = numFrame + 1
    
    #Efface le canevas
    can.delete('all')
    #Propagation du déplacements des noeuds
    for n in range(len(coordonnee)-1, 0, -1):
        coordonnee[n][0] = coordonnee[n-1][0]
        coordonnee[n][1] = coordonnee[n-1][1]
    
    #Mise à jour des coordonnées
    if direction == 'right' :
        coordonnee[0][0] += 20
    if direction == 'left' :
        coordonnee[0][0] -= 20
    if direction == 'up' :
        coordonnee[0][1] -= 20
    if direction == 'down' :
        coordonnee[0][1] += 20
    
    #Dessin de la tête du serpent et de noeuds
    can.create_rectangle(coordonnee[0][0], coordonnee[0][1], coordonnee[0][0] + 20, coordonnee[0][1] + 20,
                         outline='red', fill='red')
    
    for n in range(1,len(coordonnee)):
        can.create_rectangle(coordonnee[n][0], coordonnee[n][1], coordonnee[n][0] + 20,
                             coordonnee[n][1] + 20, outline='white', fill='blue')
    objet = []
    
    #Premier objet (la pomme)
    x = randint(1,24)
    y = randint(1,24)
    objet.append([x*20, y*20, 0])
    
    for p in range(len(objet)):
        if coordonnee[0][0] == objet[0][0] and coordonnee[p][1] == objet[p][1]:
            #Déplacement de la pomme
            objet[0][0] = randint(1,24)* 20
            objet[0][1] = randint(1,24)* 20
            #Ajout d'un noeud au serpent (à la même place que le dernier noeud)
            coordonnee.append([-20,-20]) #Caché pour l'instant
    
    game_over = False
    #On teste la position de la tête par raport aux noeuds du serpent
    for n in range(1,len(coordonnee)):
        if coordonnee[0][0] == coordonnee[n][0] and coordonnee[p][1] == coordonnee[n][1]:
            game_over = True #La partie est finie
    if game_over:
        #fin de partie
        TEXTE = "GAME OVER"
        normal_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        can.create_text(100,200,text = TEXTE, fill='red', font=normal)
    else:
        #La partie n'est pas finie
        #Calcule une nouvelle frame dans 100 ms
        tk.after(100, lambda:computeNextFrame(numFrame,coordonnee,objet))
    
    #Calcule une nouvelle frame dans 100ms
    tk.after(100, lambda:computeNextFrame(numFrame,coordonnee))
    
def right(event):
    #Modification de la variable globale direction
    global direction
    direction = 'right'
    print(direction)
    
def down(event):
    #Modification de la variable globale direction
    global direction
    direction = 'down'
    print(direction)
def up(event):
    #Modification de la variable globale direction
    global direction
    direction = 'up'
    print(direction)
def left(event):
    #Modification de la variable globale direction
    global direction
    direction = 'left'
    print(direction)
# On affiche le canevas

# On crée un environnement Tkinter
tk = Tk()
   
# On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
# Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
# intégré (ici l'environnement Tkinter)
# Les trois autres paramètres permettent de spécifier la taille et la couleur
# de fond du canevas
if __name__ == "__main__" :
    can = Canvas(tk, width=500, height=500, bg='black')
    can.pack()
    can.create_oval(100, 200, 120, 120, outline='red', fill='blue')
    #Direction par défaut
    direction = 'up'
    coordonnee = [[200, 200], [200, 220], [200, 240], [200,260]]
    computeNextFrame(0,coordonnee)
    #Appuyer sur la touche 'd' appelera la fonction right()
    tk.bind('d', right)
    tk.bind('s', down)
    tk.bind('z', up)
    tk.bind('q', left)
    
    # lancement de la boucle principale qui écoute les évènements (claviers...)
    tk.mainloop() # Cet appel doit être la derniere instruction du programme

