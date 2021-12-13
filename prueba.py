saldo=2000

while (True):
    print("1. Ingrese de dinero")
    print("2. Retiro de dinero")
    print("3. Mostrar dinero")
    print("4. Salir")
    seleccion = int(input("Elija una opción del 1 al 4: "))

    if(seleccion==1):
        montoIngreso = float(input("ingrese el dinero que desee ingresar"))
        saldo+=montoIngreso
        print(f"Nuevo saldo en la cuenta: {saldo}")
    elif(seleccion==2):
        montoRetiro = float(input("ingrese el dinero para retirar"))
        if(montoRetiro>saldo):
            print("Dinero insuficiente")
        else:
            saldo-=montoRetiro
            print(f"Nuevo saldo en la cuenta: {saldo}")
    elif(seleccion==3):
        print(f"Su dinero actual es: {saldo}")
    elif(seleccion==4):
        print("Programa terminado")
        break
    else:
        print("Error en la entrada de datos")
#array = ["Hola", 10, 20, [1,2,"adios"],21,22,23,24]
#print(array[2:-1])

# suma = 0
# for i in range(0,101):
#     suma+=i
# print(f"La suma es: {suma}")
