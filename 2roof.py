#Joao Pedro Aires de Siqueira 
#Eduardo Pavelecini Belleboni


import matplotlib.pyplot as plt
import math
from math import pi, tan
import sympy as sy
import numpy as np
from numpy import cos, sin

#A)
minimo = (25/100)
transformRAD = (180/np.pi)
x = 3
print(f"A altura minima(25% do comprimento) para um telhado de 3m é: {3*minimo}m")

#B)

comp = int(input("\nFale uma comprimento para o telhado: "))

print(f"\nA altura minima do telhado é: {comp*minimo}\n")
print("-"*30)

#C)


def triangles():
  fig, ax = plt.subplots()

  plt.grid(axis='both',which='major',color=(0.8, 0.8, 0.8, 0.5), linestyle='-', linewidth=1)
  plt.minorticks_on()
  plt.grid(axis='both',which='minor',color=(0.8, 0.8, 0.8, 0.5), linestyle='-', linewidth=1)
  for comp in range(2, 8):
    alt = comp / 4
     #transforma o angulo em RAD para graus
    angulo = math.atan(alt / comp) * transformRAD
    print(f"Altura minima para um telhado de {comp}m é: {alt}m")
    #desenhando os triangulos
    x = [0, comp, comp, 0]
    y = [0, 0, alt, 0]
    
    ax.set_title('Angulo: ' + str(round(angulo, 2)) + " graus")
    ax.plot(x, y, color="blue")

    
    
  plt.show()

 
triangles()
