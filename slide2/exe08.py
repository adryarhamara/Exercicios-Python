#Transformar a temperatura de graus Fahrenheit para celsius 
F = float(input("Entre com uma temperatura em Fahrenheit "))
C = (F - 32) * (5/9)
print("Valor em Celsius: {0}c ".format(C))