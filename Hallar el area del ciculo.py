# Desarrolle un algoritmo para hallar el area de un circulo, el usuario debe ingresar radio:
from math import pi      #Import es una palabra reservada que usa para jalar una información
r = float(input('Escriba el radio del circulo '))  #Permite poner texto al costado
area = pi*r**2
print('El área del círculo es:',format(area)) #Imprimir función