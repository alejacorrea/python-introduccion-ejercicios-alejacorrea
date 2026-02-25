# ejercicio_01.py
#
# Titulo: Ingreso a evento
#
# Crear un programa donde se solicite la edad
# y el valor pagado por un usuario. Si la edad es mayor a 18
# y pago $20.000, puede ingresar al evento.
#
# Requisitos:
# 1. Pedir la edad de la persona usando input() y convertirlo a int
# 2. Pedir el valor que pagó y convertirlo a float
# 3. verificar si la edad es mayor a 18 (usar operador >)
# 4. verificar si el pago es mayor o igual a 20000 (usar operador >=)
# 5. Usar condicional if con operador and para validad ambas condiciones
# 6. Mostrar un mensaje indicando si puede o no ingresar al envento
#
# Ejemplo de Entrada:
# Edad: 35
# Valor pagado: 25000
#
# Ejemplo de Salidad Esperada:
# Puede ingresar al evento

# Paso 1: Pedir la edad de la persona
edad = int(input("Ingrese su edad: "))
# Paso 2: Pedir el valor que pagó
valor_pagado = float(input("Ingrese el valor pagado: "))
# Paso 3 y 4: Verificar las condiciones de edad y pago
if edad > 18 and valor_pagado >= 20000:
    print("Puede ingresar al evento")   
else:    print("No puede ingresar al evento")
