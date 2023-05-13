# -*- coding: utf-8 -*-
"""
Programme Snake

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 
from tkinter import font as tkfont
from random import randint

# Modification de la variable globale direction

def right(event):
    """ Dirige le serpent vers la droite
    """
    global direction
    if not direction == 'left':
        direction = 'right'
    
def left(event):
    """ Dirige le serpent vers la gauche
    """
    global direction
    if not direction == 'right':
        direction = 'left'
    
def down(event):
    """ Dirige le serpent vers le bas
    """
    global direction
    if not direction == 'up':
        direction = 'down'
    
def up(event):
    """ Dirige le serpent vers le haut
    """
    global direction
    if not direction == 'down':
        direction = 'up'

        
# Calcule la nouvelle frame de jeu
def computeNextFrame(numFrame,coordonnee, objet,level):
    global direction

    # Effacer le canevas
    can.delete('all')
    
    # Propagation du déplacement des noeuds
    for n in range (len(coordonnee)-1,0,-1):
        coordonnee[n][0] = coordonnee[n-1][0]
        coordonnee[n][1] = coordonnee[n-1][1]
        
    # Mise à jour des coordonnées
    #Vérifie si la tête du serpent touche les bord de la fenêtre
    if direction == 'right':
        coordonnee[0][0] += 20
        if coordonnee[0][0] > 500:
            game_over = True
    if direction == 'left':
        coordonnee[0][0] -= 20
        if coordonnee[0][0] < 0:
            game_over = True
    if direction == 'up':
        coordonnee[0][1] -= 20
        if coordonnee[0][1] < 0:
            game_over = True
    if direction == 'down':
        coordonnee[0][1] += 20
        if coordonnee[0][1] > 500:
            game_over = True

    # Dessin de la tête du serpent et de noeuds
    can.create_rectangle(coordonnee[0][0], coordonnee[0][1], coordonnee[0][0] + 20, 
                         coordonnee[0][1] + 20, outline='orange', fill='orange')
    #Alterne de couleur entre chaque noeuds de serpents
    for n in range(1,len(coordonnee)):
        if n%2 == 0: 
            ligne = 'yellowgreen'
            couleur = 'yellowgreen'
        else:
            ligne = 'green'
            couleur = 'green'
        can.create_rectangle(coordonnee[n][0], coordonnee[n][1], coordonnee[n][0] + 20, 
                         coordonnee[n][1] + 20, outline= ligne, fill= couleur)    
    # Dessine les objets
    print(objet)
    for p in range(len(objet)):
        can.create_oval(objet[p][0], objet[p][1], objet[p][0] + 20, 
                         objet[p][1] + 20, outline= 'red', fill= 'red')   
    print(coordonnee[0])   
    for p in range(len(objet)):
        if coordonnee[0][0] == objet [p][0] and coordonnee[0][1] == objet [p][1]:
            objet[p][0] = randint(1,24)* 20
            objet[p][1] = randint(1,24)* 20
            # Ajout d'un noeud au serpent (à la même place que le dernier noeud)
            coordonnee.append([-20, -20]) # Caché pour l'instant
            level+=1
    game_over = False     
    # On test la position de la tête par rapport aux noeuds du serpent
    for n in range(1,len(coordonnee)):
        #Si la tête se situe dans les même coordonnées que un de ses noeuds ou inversement, Game over
        if coordonnee[0][0] == coordonnee [n][0] and coordonnee[p][1] == coordonnee [n][1]:
            game_over = True # La partie est finie
            
        if coordonnee[0][0] >= 500 or coordonnee[0][0] < 0 or coordonnee[0][1] >= 500 or coordonnee[0][1] < 0:
            game_over = True
    
    if game_over : 
        # Fin de partie, affichage du message 
        TEXTE = "T'es nul"
        normal_font = tkfont.Font(family="Helvetica", size=50, weight="bold")
        can.create_text(250,200,text = TEXTE, fill='black',  font=normal_font)
    else:
        # La partie n'est pas finie donc affiche une nouvelle frame
        tk.after(75, lambda:computeNextFrame(numFrame,coordonnee, objet,level))

    
    if not game_over:
        texte_compteur = level
        normal_font = tkfont.Font(family="Helvetica", size=45, weight="bold")
        can.create_text(480,40,text = level, fill='black',  font=normal_font)
        
        
if __name__ == "__main__":
    # On crée un environnement Tkinter
    tk = Tk()
    # On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
    can = Canvas(tk, width=500, height=500, bg='sienna')

    # Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
    # intégré (ici l'environnement Tkinter)
    # Les trois autres paramètres permettent de spécifier la taille et la couleur
    # de fond du canevas
    # On affiche le canevas
    can.pack()
    
    # Direction par défaut
    direction = 'up' 
    
    coordonnee = [[200, 200], [200, 220], [200, 240], [200,260]]
    objet = []
    
    # Premier objet (la pomme)
    x = randint(1,24)
    y = randint(1,24)
    objet.append([x*20, y*20])
    # Construction de la première étape de simulation
    computeNextFrame(0,coordonnee, objet,4)
    
    tk.bind('<d>', right) #Droite 
    tk.bind('<q>', left) #Gauche
    tk.bind('<s>', down) #Bas
    tk.bind('<z>', up) #Haut
    
    # lancement de la boucle principale qui écoute les évènements (claviers...)
    tk.mainloop() # Cet appel doit être la derni�ere instruction du programme
