def compara(numero1, numero2):
    if numero1 > numero2 : return print(f"{numero1} es mayor que {numero2}")
    elif numero1 < numero2: return  print(f"{numero1} es menor que {numero2}")
    else: return print(f"{numero1} y {numero2} son iguales")


numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

compara(numero1=numero1, numero2=numero2)