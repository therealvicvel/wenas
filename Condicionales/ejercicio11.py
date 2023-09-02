nombreArticulo=""
clave=0
precioOriginal=0
precioDescuento=0
nombreArticulo=input("Ingrese el nombre del artículo adquirido: ")
clave=int(input("Ingrese la clave: "))
precioOriginal=int(input("Ingrese el precio del artículo: "))
if(clave==1):
    precioDescuento=precioOriginal-(precioOriginal*0.10)
    print("El precio del artículo con descuento es: " , precioDescuento)
elif(clave==2):
    precioDescuento=precioOriginal-(precioOriginal*0.20)
    print("El precio del artículo con descuento es: " , precioDescuento)