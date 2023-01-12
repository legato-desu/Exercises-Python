# Mayor de 3 numeros
"""
Escribir un programa que solicite al usuario 3 números, 
compararlos y decir cual es mayor.
"""
numero_1 = input("Ingrese el primer numero: ")
numero_2 = input("Ingrese el segundo numero: ")
numero_3 = input("Ingrese el tercer numero: ")

try:
    numero_1=int(numero_1)
    numero_2=int(numero_2)
    numero_3=int(numero_3)
except:
    print("Ingrese un numero entero ")
    exit()
if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"El primer numero > {numero_1} < es mayor")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"El segundo numero > {numero_2} < es mayor")     
else:
    print(f"El tercer numero > {numero_3} < es mayor")