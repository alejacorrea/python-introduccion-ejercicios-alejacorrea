# ejercicio_02.py
#
# Titulo: Calculadora precio con Iva
#
# Descripcion:
# Crear un programa que calcule el precio final de un prodcuto con IVA incluido.
# El usuario ingresa el precio sin IVA y el programa calcula cuanto es el IVA y su precio total.
# El IVA en colombia es del 19%
#
# Requisitos:
# 1. Definir la variable VALOR_IVA = 19 como constante
# 2. Pedir el precio del producto sin IVA
# 3. Calcular el valor del IVA: precio * (VALOR_IVA / 100)
# 4. Calcular precio total: precio + iva
# 5. Mostrar precio, IVA y precio total
#
# Ejemplo de Entrada:
# Precio sin IVA: 45000
#
# Ejemplo de Salida Esperada:
# Precio: $45000
# IVA (19%): $8550
# Precio total: $53550

# Paso 1: Definir la variable VALOR_IVA
VALOR_IVA = 19
# Paso 2: Pedir el precio del producto sin IVA
precio_sin_iva = float(input("Ingrese el precio del producto sin IVA: "))
# Paso 3: Calcular el valor del IVA
iva = precio_sin_iva * (VALOR_IVA / 100)
# Paso 4: Calcular precio total
precio_total = precio_sin_iva + iva
# Paso 5: Mostrar precio, IVA y precio total
print(f"Precio: ${precio_sin_iva}")
print(f"IVA ({VALOR_IVA}%): ${iva}")
print(f"Precio total: ${precio_total}")
