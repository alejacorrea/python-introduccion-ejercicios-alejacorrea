# ejercicio_09.py
#
# Titulo: Calcular el perimetro y area de un circulo
#
# Descripcion:
# Crear un programa que calcule el perimetro y area de un circulo dado su radio.
#
# Requisitos:
# 1. Definir la constante PI = 3.14159 
# 2. Pedir el radio del circulo usando input() y convertirlo a float
# 3. Calcular el area usando la formula: area = PI * radio ** 2
# 4. Calcular perimetro usando la formula: perimetro = 2 * PI * radio
# 5. Mostrar ambos resultador con 2 decimales usando f-strings
# 
# Ejemplo de Entrada:
# Ingresa el radio del circulo: 5
# 
# Ejemplo de Salida Esperada:
# Area del circulo: 78.54
# Perimetro del circulo: 31.42 

# Paso 1: Definir la constante PI
PI = 3.14159
# Paso 2: Pedir el radio del circulo usando input() y convertirlo a float
radio = float(input("Ingresa el radio del circulo: "))
# Paso 3: Calcular el area usando la formula: area = PI * radio ** 2
area = PI * radio ** 2
# Paso 4: Calcular perimetro usando la formula: perimetro = 2 * PI * radio
perimetro = 2 * PI * radio
# Paso 5: Mostrar ambos resultador con 2 decimales usando f-strings
print(f"Area del circulo: {area:.2f}")
print(f"Perimetro del circulo: {perimetro:.2f}")