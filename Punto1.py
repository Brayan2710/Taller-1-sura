n=0
contadorNegativos=0
contadorPositivos=0

for i in range(2):

    Numeros=int(input("Digite un numero "))
    if (Numeros<0):
        contadorNegativos+1
    elif(Numeros>0):
        contadorPositivos+1
    else:
        print("eso no es un numero vuelva a digitarlo ")
print("La Cantidad de numeros  negativos es de  ",contadorNegativos)
    




    
