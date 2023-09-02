monto=0
cuotaAPagar=0
monto=int(input("Ingrese el monto: "))
if(monto<50000):
    cuotaAPagar=(monto*0.03)
    print("La cuota a pagar es: " , cuotaAPagar)
elif(monto>50000):
    cuotaAPagar=(monto*0.02)
    print("La cuota a pagar es: " , cuotaAPagar)