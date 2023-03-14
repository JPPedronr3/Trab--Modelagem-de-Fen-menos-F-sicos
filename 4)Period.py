#Joao Pedro Aires de Siqueira 
#Eduardo Pavelecini Belleboni
#4)
import matplotlib.pyplot as grv
import math
from math import pi, tan
import sympy as sy
import numpy as np
from numpy import cos, sin



def wave():
  while True:
    x = int(input("Digite uma quantidade de periodos entre 1 e 5: "))
    if x >= 1 and x <= 5:
      break
  
  sc = (2*x) - 1
  tangente = x-1
  z = np.linspace(0,sc*180, 1000, endpoint=True)
  X = np.linspace(-pi,sc*pi, 1000, endpoint=True)
  coseno = cos(X)
  sen = sin(X)
  print("Opçoes:")
  print("[1] Cosseno")
  print("[2] Seno")
  print("[3] Tangente")
  option = int(input("Escolha: [1] [2] [3]"))
  if option == 1:
      grv.plot(z,  coseno, color="blue", linewidth=2.0, linestyle="-")
      grv.title("Cosseno")
      grv.show()
      
  if option == 2:
      grv.plot(z, sen, color="green", linewidth=2.0, linestyle="-")
      grv.title("Seno")
      grv.show()
      
  if option == 3:
      tgz = np.linspace(0, tangente*180, 1000)
      x = np.linspace(-pi, tangente*pi, 1000)
      grv.plot(tgz, (np.tan(x)),color = 'black')
      grv.title("Tangente")
      grv.ylim(-4,4)
      grv.show()
wave()