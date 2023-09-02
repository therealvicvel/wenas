nombre=""
edad=0
sexo=0
nombre=(input("Ingrese aquí su nomrbre: "))
edad=int(input("Ingrese aquí su edad: "))
sexo=int(input("Ingrese aquí su sexo. Utilize 1 para femenino y 2 para masculino: "))
if(sexo==2 and edad>=18):
    print("Su nombre es: " , nombre)
elif(sexo==2 and edad<18):
    print("Su nombre es: " , nombre)
    print("Su edad es: " , edad)
elif(sexo==1):
    print("Su nombre es: " , nombre)
    print("Su edad es: " , edad)