##3.Construir un programa para ir de compras en un supermercado
#que permita la construcción del siguiente MENU:
#1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.8)
#2. Digitar 2 para mostrar todos los productos registrados (+0.8)
#3. Digitar 0 para SALIR

print("*******MENU*******************")
print("Supermercado")
print("1.#1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.8)")
print("2. Digitar 2 para mostrar todos los productos registrados (+0.8)")
print("3. Digitar 0 para SALIR")

opcion=0
venta=[]
while(opcion!=3):
    producto={}
    
    opcion=int(input("Digite una opcion del menu          "))
    if(opcion==1):
        producto['codigo']=int(input("Ingrese  el codigo "))
        producto['Nombre']=input("Ingrese el nombre del producto")
        producto['precio']=int(input("Ingrese  el precio "))
        venta.append(producto)
    elif(opcion==2):
        print(venta)
    elif(opcion==3):
        print("SALIENDOOO")
    else:
        print("Opcion no valida")    
