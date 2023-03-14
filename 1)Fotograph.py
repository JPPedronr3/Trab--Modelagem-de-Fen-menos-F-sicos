#Joao Pedro Aires de Siqueira 
#Eduardo Pavelecini Belleboni

import matplotlib.pyplot as grf
import math
from math import pi, tan
import sympy as sy
import numpy as np
from numpy import cos, sin

#Exercicio 1 A)

#transforma radiano para angulo em graus
transform = (180/np.pi)

tan = 200/50
ang = (math.atan(tan))*transform
print("O angulo do fotografo a uma distancia de 50m é:", end=" ")
print(f"{ang:.2f}°")

x1=np.array([0,50,50,0])
y1=np.array([0,0,200,0])

fig1= grf.figure(1)
ax1=fig1.add_subplot(111)

ax1.axis('square')
grf.plot(x1,y1,color=[0/255,0/255,0/255])

grf.xlim([-20,70])
grf.ylim([-20,220])

grf.grid(axis='both',which='major',color=(0.8, 0.8, 0.8, 0.5), linestyle='-', linewidth=0.8)
grf.minorticks_on()
grf.grid(axis='both',which='minor',color=(0.8, 0.8, 0.8, 0.5), linestyle='-', linewidth=0.8)

grf.show() 
print("\n-="*30)

#descobrindo o angulo(variavel)

def angx(catO,catA):
  tangente = catO/catA
  radiano = math.atan(tangente)
  ang = radiano * transform
  return ang

y = int(input("Digite a altura do foguete: "))

angulo = angx(y,50)

print(f"o fotografo precisa de um agulo de {angulo} para conseguir tirar a foto")
print("\n O triângulo ficara dessa forma: \n")

#C) plotar o triangulo

x1=np.array([0,50,50,0])
y1=np.array([0,0,y,0])

fig1= grf.figure(1)
ax1=fig1.add_subplot(111)

ax1.axis('square')
grf.plot(x1,y1,color=[0/255,100/255,200/255])

if y > 50:
  grf.xlim([-50,y])
else:
  grf.xlim(-20,60)  
grf.ylim([-20,y+10])

grf.grid(axis='both',which='major',color=(0.8, 0.8, 0.8, 0.5), linestyle='-', linewidth=1)
grf.minorticks_on()
grf.grid(axis='both',which='minor',color=(0.8, 0.8, 0.8, 0.5), linestyle=':', linewidth=1)



grf.show() 

