#13.	Calcular el total que una persona debe pagar en una venta de llantas,
# si el precio de cada llanta es de $80.000 si se compran menos de 5 llantas y de $70.000 si se compran 5 o más.

nroLlantas=int(input("Ingresar cantidad de llantas"))
if(nroLlantas<=0):
    print("largo de aquipobre")
elif(nroLlantas<5):
    precioLlantas1=80000
    totalPago=nroLlantas*precioLlantas1
    print(totalPago)
elif(nroLlantas>=5):
    precioLlantas2=70000
    totalPago2=nroLlantas*precioLlantas2
    print(totalPago2)
    