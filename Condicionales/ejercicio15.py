edad=0
genero=""
numPulsaciones=0
genero=(input("Ingrese su género: "))
edad=int(input("Ingrese su edad: "))
if(genero=="Femenino"):
    numPulsaciones=(220-edad)/10
    print("Su número de pulsaciones son: " , numPulsaciones)
elif(genero=="Masculino"):
    numPulsaciones=(210-edad)/10
    print("Su número de pulsaciones es: " , numPulsaciones)
else:
    print("Tenga en cuenta que sólo se permiten las palabras Femenino y Masculino con su primera letra en mayúsculas. ")