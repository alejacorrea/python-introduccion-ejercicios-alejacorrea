# ejercicio_10.py
#
# Titulo: Calcular sueldo por horas
# 
# Descripcion:
# Calcular el sueldo mensual de un Colaborador conociendo la cantidad de horas trabajdas
# y el pago por hora
#
# Requisitos:
# 1. Pedir la cantidad de horas trabajadas en el usando input() y convertir a float
# 2. Pedir el valor que se paga por cada hora trabajada y convertir a float
# 3. Calcular el sueldo mensual multiplicando las horas por el valor por hora
# 4. Mostrar el resultado del sueldo mensual
#
# Ejemplo de Entrada:
# Horas trabajadas en el mes: 160
# Valor por hora: 15000
#
# Ejemplo de Salida Esperada:
# El sueldo mensual del colaborador es: $2400000

# Paso 1: Pedir la cantidad de horas trabajadas en el usando input() y convertir a float
horas_trabajadas = float(input("Horas trabajadas en el mes: "))
# Paso 2: Pedir el valor que se paga por cada hora trabajada y convertir a float
valor_por_hora = float(input("Valor por hora: "))
# Paso 3: Calcular el sueldo mensual multiplicando las horas por el valor por hora
sueldo_mensual = horas_trabajadas * valor_por_hora
# Paso 4: Mostrar el resultado del sueldo mensual
print(f"El sueldo mensual del colaborador es: ${sueldo_mensual}")


