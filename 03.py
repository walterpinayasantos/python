'''Escribir un programa que permita ingresar el nombre, edad y estatura
de una persona, y pueda imprimir por consola los datos y el tipo de
dato al que corresponda'''
nombre = input("Nombre: ")
edad = int(input("Edad: "))
estatura = float(input("Estatura: "))
print(F"{nombre} tiene {edad} años y mide {estatura} metros")
print(nombre, type(nombre))
print(edad, type(edad))
print(estatura, type(estatura))
