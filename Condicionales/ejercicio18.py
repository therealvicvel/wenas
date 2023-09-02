descuento=0
precioFinal=0
numComputadorasCompradas=0
precioConDescuento=0
precioComputadora=11000
numComputadorasCompradas=int(input("Señor comprador, ingrese la cantidad de computadoras que adquirió: "))
precioFinal=precioComputadora*numComputadorasCompradas
if(numComputadorasCompradas<5):
    descuento=precioFinal*0.10
    precioConDescuento=precioFinal-descuento
    print("Su descuento será del 10% y la cifra es: " , descuento)
    print("El precio final es: " , precioConDescuento)
elif(numComputadorasCompradas>=5 and numComputadorasCompradas<10):
    descuento=precioFinal*0.20
    precioConDescuento=precioFinal-descuento
    print("Su descuento será del 20% y la cifra es: " , descuento)
    print("El precio final es: " , precioConDescuento)
elif(numComputadorasCompradas>10):
    descuento=precioFinal*0.40
    precioConDescuento=precioFinal-descuento
    print("Su descuento será del 40% y la cifra es: " , descuento)
    print("El precio final es: " , precioConDescuento)