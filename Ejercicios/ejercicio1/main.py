def es_primo(numero):
    #Validacion
    if numero % 2 != 0: print(False)
    else: print(True)

numero = int(input("Ingresa un numero: ")) #leemos un numero de tipo entero

es_primo(numero) #Pasamos la variable 'numero' como parametro a la funcion