# Créé par Clément, le 24/03/2020 en Python 3.4
from tkinter import*

fenetre = Tk()

#canvas
canvas = Canvas(fenetre, width=1450, height=700,background='black')
canvas.pack()

for ligne in range(1, 13):
  if ligne == 2:
    coul = 'blue2'
  elif ligne == 3:
    coul = 'blue2'
  elif ligne == 4:
    coul = 'blue2'
  elif ligne == 6:
    coul = 'yellow'
  elif ligne == 7:
    coul = 'yellow'
  elif ligne == 9:
    coul = 'Deeppink2'
  elif ligne == 10:
    coul = 'Deeppink2'
  elif ligne == 11:
    coul = 'Deeppink2'
  else:
    coul = 'white'
  canvas.create_rectangle(100*ligne, 0, 100*ligne+100, 100,fill=coul)

for ligne in range(1, 13):
  if ligne == 2:
    coul = 'cyan'
  elif ligne == 3:
    coul = 'cyan'
  elif ligne == 4:
    coul = 'cyan'
  elif ligne == 6:
    coul = 'grey'
  elif ligne == 7:
    coul = 'grey'
  elif ligne == 8:
    coul = 'grey'
  elif ligne == 10:
    coul = 'orange'
  elif ligne == 11:
    coul = 'orange'
  else:
    coul = 'white'
  canvas.create_rectangle(100*ligne, 600, 100*ligne+100, 700,fill=coul)

for colonne in range(1, 6):
  if colonne == 1:
    coul = 'red'
  elif colonne == 2:
    coul = 'red'
  elif colonne == 4:
    coul = 'purple'
  elif colonne == 5:
    coul = 'purple'
  else:
    coul = 'white'
  canvas.create_rectangle(100, 100*colonne, 200, 100*colonne+100,fill=coul)

for colonne in range(1, 6):
  if colonne == 1:
    coul = 'brown'
  elif colonne == 2:
    coul = 'brown'
  elif colonne == 4:
    coul = 'green'
  elif colonne == 5:
    coul = 'green'
  else:
    coul = 'white'
  canvas.create_rectangle(1200, 100*colonne, 1300, 100*colonne+100,fill=coul)

canvas.create_text(700, 350, text="MONOPOLY", font="Arial 70 italic", fill="white")



fenetre.mainloop()