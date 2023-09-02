totalAPagar=0
totalSinDescuento=0
precioCamisas=0
camisas=0
descuento=0
precioCamisas=int(input("Ingrese el valor de una camisa: "))
camisas=int(input("Ingrese la cantidad de camisas: "))
totalSinDescuento=precioCamisas*camisas
if(camisas>3):
    descuento=totalSinDescuento-(totalSinDescuento*0.20)
    totalAPagar=totalSinDescuento-descuento
    print("El valor a pagar es: " , descuento)
    print("El valor sin descuento sería de: " , totalSinDescuento)
elif(camisas<3):
    descuento=totalSinDescuento-(totalSinDescuento*0.10)
    totalAPagar=totalSinDescuento-descuento
    print("El valor a pagar es: " , totalAPagar)
    print("El valor sin descuento sería de: " , totalSinDescuento)