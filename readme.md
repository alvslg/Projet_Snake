from tkinter import * 

def right(event):
    # Modification de la variable globale direction
    global perso_x2
    global perso_x
    perso_x +=1
    perso_x2 +=1
   

def left(event):
    # Modification de la variable globale direction
    global perso_x2
    global perso_x
    perso_x -=1
    perso_x2 -=1

    
def down(event):
    # Modification de la variable globale direction
    global perso_y2
    global perso_y
    perso_y +=1
    perso_y2 +=1
  
def up(event):
    # Modification de la variable globale direction
    global perso_y2
    global perso_y
    perso_y -=1
    perso_y2 -=1

def moteur():
    global direction
    dessine_laby()
    dessine_perso()
    fenetre.after(100, moteur)

def dessine_perso():
    global perso_x
    global perso_y
    print(perso_x, perso_y)
    cercle = canvas.create_oval(perso_x,perso_y,perso_x2,perso_y2,fill="red", outline="#FFF", width=4)

def dessine_laby():
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
    

fenetre = Tk()

canvas = Canvas(fenetre, width=600, height=480, background='white')


ligne1 = canvas.create_line(150, 125, 150, 400)
ligne2 = canvas.create_line(200, 125, 450, 125)
ligne3 = canvas.create_line(450, 425, 450, 175)
ligne4 = canvas.create_line(150, 425, 450, 425)

txt = canvas.create_text(300, 20, text="Labyrinthe", font="Arial 24 italic", fill="black")
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


pos_perso =[0, 0]
perso_x = 100
perso_y = 100
perso_x2 = 25
perso_y2 = 25
dessine_laby()
moteur()
canvas.pack()
fenetre.bind('<d>', right) 
fenetre.bind('<q>', left) 
fenetre.bind('<s>', down) 
fenetre.bind('<z>', up)

fenetre.mainloop()      
