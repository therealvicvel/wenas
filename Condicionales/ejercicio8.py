cantidadInvertida=0
intereses=0
cantidadFinal=0
cantidadInvertida=int(input("Ingrese la cantidad de dinero que invirtió: "))
cantidadFinal=int(input("Ingrese la cantidad final obtenida con intereses: "))
intereses=cantidadFinal-cantidadInvertida
if(intereses<=0):
    print("ERROR. ")
elif(cantidadInvertida<=0):
    print("ERROR. ")
elif(intereses<=7000):
    print("Sus ganancias son: " , intereses)
    print("Como los intereses son inferiores a 7000 el usuario decide no reinvertir su dinero. ")
elif(intereses>=7000):
    print("Sus ganancias son: " , intereses)
    print("Como los intereses son superiores a 7000 el usuario decide reinvertir su dinero. ")