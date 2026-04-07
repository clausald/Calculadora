import Operaciones 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Seleccione una operación: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingrese el número de la operación: ")
if opcion == '1':
    resultado = Operaciones.sumar(num1, num2)

elif opcion == "2":
    resultado = Operaciones.restar(num1, num2)

elif opcion == "3":
    resultado = Operaciones.multiplicar(num1, num2)

elif opcion == "4":
    resultado = Operaciones.dividir(num1, num2)

else:
    resultado = "Opción no válida"

print("El resultado es:", resultado)