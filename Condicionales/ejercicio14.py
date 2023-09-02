numAzar=0
valorProducto=0
valorTotal=0
articulo=""
articulo=input("Ingrese el nombre del producto adquirido: ")
valorProducto=int(input("¿Cuánto le costó el producto? "))
numAzar=int(input("Ingrese un número al azar: "))
if(numAzar<=0):
    print("ERROR: INGRESE UN NÚMERO VÁLIDO. ")
elif(valorProducto<=0):
    print("ERROR: INGRESE UN NÚMERO VÁLIDO. ")
elif(numAzar<=74):
    descuento=valorProducto*0.15
    valorTotal=valorProducto-descuento
    print("El valor sin descuento es: " , valorProducto)
    print("El valor final es: " , valorTotal)
    print("El descuento es de: " , descuento)
elif(numAzar>74):
    descuento=valorProducto*0.20
    valorTotal=valorProducto-descuento
    print("El valor sin descuento es: " , valorProducto)
    print("El valor final es: " , valorTotal)
    print("El descuento es de: " , descuento)