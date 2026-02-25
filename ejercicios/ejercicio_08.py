# ejercicio_08.py
#
# Titulo: Convertir minutos a horas y minutos
#
# Descripcion:
# Crear un programa que solicite
# a la persona una cantidad de minutos y la
# convierta a horas y minutos.
#
# Requisitos:
# 1. Pedir al usuario la cantidad de minutos (int)
# 2. Calcular las horas usando division entera (//): minutos // 60
# 3. Calcular los minutos restantes usando modulo (%): minutos % 60
# 4. Mostrar el resultado en formato horas y minutos
#
# Ejemplo de Entrada:
# Minutos: 135
#
# Ejemplo de Salida Esperada:
# 135 minutos equivalen a 2 horas y 15 minutos

# Paso 1: Pedir al usuario la cantidad de minutos (int)
minutos = int(input("Minutos: "))
# Paso 2: Calcular las horas usando division entera (//): minutos // 60
horas = minutos // 60
# Paso 3: Calcular los minutos restantes usando modulo (%): minutos % 60
minutos_restantes = minutos % 60
# Paso 4: Mostrar el resultado en formato horas y minutos
print(f"{minutos} minutos equivalen a {horas} horas y {minutos_restantes} minutos")