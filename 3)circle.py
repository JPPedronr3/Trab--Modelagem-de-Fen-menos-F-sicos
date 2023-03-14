#Joao Pedro Aires de Siqueira 
#Eduardo Pavelecini Belleboni

import matplotlib.pyplot as grt
import math
from math import pi, tan
import sympy as sy
import numpy as np
from numpy import cos, sin

#3)

transformar_radiano = pi/180

x = int(input("Digite um ângulo: "))
#transforma angulo para radiano
angulo = x * transformar_radiano

def circle(angulo):

  #the background sqaures
  
  grt.grid(axis='both',which='major',color=(0.8, 0.8, 0.8, 0.5), linestyle='-', linewidth=1)
  grt.minorticks_on()
  grt.grid(axis='both',which='minor',color=(0.8, 0.8, 0.8, 0.5), linestyle='-', linewidth=1)

  angle = np.linspace(0,2*pi,100)
  xs = cos(angle)
  ys = sin(angle)
  raio = 0.5
  arco_angles = np.linspace(0, angulo, 20)
  arco_xs = raio * cos(arco_angles)
  arco_ys = raio * sin(arco_angles)

  grt.plot([cos(angulo),cos(angulo)],[0,sin(angulo)], color = 'purple')
  grt.plot([0,cos(angulo)],[0,0],color = 'blue')
  grt.plot([1, 1], [0,np.tan(angulo)], color = 'red')

  grt.plot(xs,ys, color="black")

  grt.plot([0, 0], [1, -1], color = "black")
  grt.plot([0, 1], [0, 0], color = 'black')

  grt.plot([0,cos(angulo)], [0,sin(angulo)], color = "black")

  grt.plot([cos(angulo),1],[sin(angulo),np.tan(angulo)],color = "black")
  grt.plot([0,cos(angulo)],[0,0],color = 'blue')

  grt.plot(arco_xs, arco_ys, color = 'black', lw = 1.5)
  grt.gca().annotate(r'0', xy=(np.cos(angulo/2) * 0.5, np.sin(angulo/2) * 0.5), xycoords='data', fontsize=12)
  grt.legend(["sin","cos","tan"])

#Caso o angulo seja muito proximo de 90, ele aumentara a visao para poder ter noçao da dimensao
  
  if x > 65:
    grt.xlim(-4,4)
    grt.ylim(-4,4)
  else:
    grt.xlim(-2,2)
    grt.ylim(-2,2)
  grt.show()

circle(angulo)