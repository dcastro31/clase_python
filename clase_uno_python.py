# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Variables

a = 3
print(type(a))
a = "Hola"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))
# Type es utiñizado para saber el tipo de dato utilizado

print('Hola mundo')
# Print es para immprimir en consola y se usa mucho la comilla simple

# Operaciones

# Suma
a = 5
b = 2
c = a + b
print(c)

# Resta
a = 5
b = 2
c = a - b
print(c)

# Multiplicacion
a = 5
b = 2
c = a * b
print(c)

# Division 
a = 5
b = 2
c = a / b
print(c)

# Division parte entera
a = 5
b = 2
c = a // b
print(c)

# Potencia
a = 2
c = a ** 6
print(c)

# Raiz cuadrada
a = 16
b = a ** (1/2)
print(b)

import math
raiz = math.sqrt(a)
print(raiz)

# Raiz cubica
a = 16
b = a ** (1/3)
print(b)

# Tipos de datos

# String str

a = "Hola mundo"
b = 'Hola mundo'
c = "I can't do it"
d = 'alias "Deyner"'

# Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False

# Conversiones entre tipos de datos

# Convertir de x a entero

a = '3'
b = int(a)
print(type(b))

# Convertir de x a decimal
a = 3
b = float(a)
print(type(b))

# Convertir de x a String
a = 3
b = str(a)
print(type(b))

# Concatenaciones
a = 'hola'
b = 'mundo'
c = a + ' ' + b

a = 'hola'
b = a * 5
print(b)

# Capturar por pantalla
nombre = input('Digite su nombre: ')
print('Hola',nombre, sep='**', end='ROBERTO')


nombre = input('Digite su nombre: ')
print('Hola' + nombre)

# Interpolación

nombre = input('Digite su nombre: ')
print(f'Su nombre es {nombre}')


# HUA que sume dos numeros e impima su resultado

numero_uno = int(input('Digite el número uno: '))
numero_dos = int(input('Digite el número dos: '))
suma = numero_uno + numero_dos
print(f'El resultado de sumar {numero_uno} + {numero_dos} es: {suma}')



# HUA que lea un número y lo eleve al cuadrado

num = int(input("Ingresa número: "))
alcuadrado = num ** 2
print(f"{num} elevado al cuadrado es: {alcuadrado}")


# HUA que tome el valor de un producto, le aplique el 20%
# de descuento, imprima el valor del producto inicial,
# el valor con descuento y el valor ahorrado


p_value = int(input("Ingrese el valor del producto: $"))
descuento = p_value * 0.20
valor_final = p_value - descuento
print(f'El valor del producto inicial es de: ${p_value:,}')
print(f"El valor ahorrado es de: ${descuento:,}")
print(f"El valor con el descuento aplicado es de: ${valor_final:,}")

