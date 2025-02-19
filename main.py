
print("hola aquí andamos") 
print()#esto es un salto de linea, 
print('haciendo el gambita un raro con er python')

'''
esto es un comentario de varias lineas
'''
print()#esto es un salto de linea,

nombre = "Pablo"
len(nombre)#devuelve la longitud de la cadena
print("NOMBRE: "+nombre)

edad = 34

print("EDAD: "+str(edad))

isconductor = True
ismarika = False

numero1 = 3
numero2 = 4

print("SUMA: "+str(numero1+numero2))#str une a cadena
print(numero1/numero2)#division
print(numero1//numero2)#division entera, solo devuelve entero
print(numero1%numero2)#devuelve el resto de la division
print(numero1*numero2)#multiplicacion
print(numero1**numero2)#exponenciacion
print(numero1** 0.5)#raiz cuadrada

#operadores de comparacion

numero=3

if numero < 2 :
    print("es menor")
else:
    print("es mayor")