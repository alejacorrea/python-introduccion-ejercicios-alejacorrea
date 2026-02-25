# ejercicio_07.py
#
# Titulo: Calculadora de descuentos en una compra
#
# Descripcion:
# Crear un programa en donde el cliente recibe un 10% de descuento si su valor de compra es mayor a $200000.
# El programa debe calcular el valor total a pagar.
#
#Requisitos:
# 1. Pedir al usuario el valor de la compra usando input() y convertirlo a float
# 2. Definir una constante DESCUENTO_PORCENTAJE = 10
# 3. Verificar si el valor de la compra es mayor a 200000 usando if
# 4. si la condicion se cumple, calcular el descuento: valor * (DESCUENTO_PORCENTAJE / 100)
# 5. Restar el descuento al valor original para obtener el total a pagar
#
# Ejemplo de Entrada:
# Valor de la compra: 300000
#
# Ejemplo de Salida Esperada:
# Tienes un descuento del 10%
# Total a pagar: $270000

# Paso 1: Pedir al usuario el valor de la compra usando input() y convertirlo a float
valor_compra = float(input("Valor de la compra: "))
# Paso 2: Definir una constante DESCUENTO_PORCENTAJE
DESCUENTO_PORCENTAJE = 10
# Paso 3: Verificar si el valor de la compra es mayor a 200000 usando if
if valor_compra > 200000:
# Paso 4: si la condicion se cumple, calcular el descuento
    descuento = valor_compra * (DESCUENTO_PORCENTAJE / 100)
    print(f"Tienes un descuento del {DESCUENTO_PORCENTAJE}%")
# Paso 5: Restar el descuento al valor original para obtener el total a pagar
    total_a_pagar = valor_compra - descuento
else:    total_a_pagar = valor_compra
print(f"Total a pagar: ${total_a_pagar}")