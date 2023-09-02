cantidadProducto=0
valorProducto=0
valorDescuento=0
totalAPagar=0
cantidadProducto=int(input("Ingrese el número de productos que adquirió: "))
valorProducto=int(input("Ingrese el valor de producto que adquirió: "))
if(cantidadProducto<=0):
    print("ERROR: Ingrese un carácter válido: ")
elif(valorProducto<=0):
    print("ERROR: Ingrese un carácter válido: ")
elif(cantidadProducto<=5):
    totalAPagar=(cantidadProducto*valorProducto)-(cantidadProducto*valorProducto*0.05)
    print("El valor total que usted deberá pagar es: " , totalAPagar)
    print("El valor total sin descuento sería de: " , cantidadProducto*valorProducto)
    print("El porcentaje del descuento es 5% ")
elif(cantidadProducto<=8):
    totalAPagar=(cantidadProducto*valorProducto)-(cantidadProducto*valorProducto*0.08)
    print("El valor total que usted deberá pagar es: " , totalAPagar)
    print("El valor total sin descuento sería de: " , cantidadProducto*valorProducto)
    print("El porcentaje del descuento es 8% ")
elif(cantidadProducto>=15):
    totalAPagar=(cantidadProducto*valorProducto)-(cantidadProducto*valorProducto*0.15)
    print("El valor total que usted deberá pagar es: " , totalAPagar)
    print("El valor total sin descuento sería de: " , cantidadProducto*valorProducto)
    print("El porcentaje del descuento es 15% ")