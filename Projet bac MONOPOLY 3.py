# Créé par Clément, le 24/03/2020 en Python 3.4
from tkinter import*

fenetre = Tk()

#canvas
canvas = Canvas(fenetre, width=1450, height=700,background='black')
canvas.pack()

for ligne in range(1, 13):
  if ligne in [2, 3, 4]:
    coul = 'blue2'
  elif ligne in [6, 7]:
    coul = 'yellow'
  elif ligne in [9, 10, 11]:
    coul = 'Deeppink2'
  else:
    coul = 'white'
  canvas.create_rectangle(100*ligne, 0, 100*ligne+100, 100,fill=coul)

for ligne in range(1, 13):
  if ligne in [2, 3, 4]:
    coul = 'cyan'
  elif ligne in [6, 7, 8]:
    coul = 'grey'
  elif ligne in [10, 11]:
    coul = 'orange'
  else:
    coul = 'white'
  canvas.create_rectangle(100*ligne, 600, 100*ligne+100, 700,fill=coul)

for colonne in range(1, 6):
  if colonne in [1, 2]:
    coul = 'red'
  elif colonne in [4, 5]:
    coul = 'purple'
  else:
    coul = 'white'
  canvas.create_rectangle(100, 100*colonne, 200, 100*colonne+100,fill=coul)

for colonne in range(1, 6):
  if colonne in [1, 2]:
    coul = 'brown'
  elif colonne in [4, 5]:
    coul = 'green'
  else:
    coul = 'white'
  canvas.create_rectangle(1200, 100*colonne, 1300, 100*colonne+100,fill=coul)

canvas.create_text(700, 350, text="MONOPOLY", font="Arial 70 italic", fill="white")



fenetre.mainloop()