caloriasAlDia=0
calorias1=0
calorias2=0
actividad1=0
actividad2=0
actividad1=int(input("¿Cuántos minutos duerme al día? "))
actividad2=int(input("¿Cuántos minutos se sienta a reposar al día? "))
calorias1=1.08*actividad1
calorias2=1.66*actividad2
if(actividad1<=480 and actividad2<=240):
    caloriasAlDia=calorias1+calorias2
    print("Sus calorías al día son: " , caloriasAlDia)
elif(actividad1>=480 and actividad2<=240):
    caloriasAlDia=calorias1+calorias2
    print("Sus calorías al día son: " , caloriasAlDia)
elif(actividad1<=480 and actividad2>=240):
    caloriasAlDia=calorias1+calorias2
    print("Sus calorías al día son: " , caloriasAlDia)
elif(actividad1>=480 and actividad2>=240):
    caloriasAlDia=calorias1+calorias2
    print("Sus calorías al día son: " , caloriasAlDia)