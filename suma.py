# Solicitar al usuario que ingrese dos números
numero1 = input("Ingrese el primer número: ")
numero2 = input("Ingrese el segundo número: ")
try:
    resultado_str = str(numero1 + numero2)
    print("La suma como cadena es:", resultado_str)

except ValueError:
    print("Error: Ingresa números válidos.")