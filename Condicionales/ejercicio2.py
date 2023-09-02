nombre=""
edad=0
sexo=0
estadoCivil=0
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
sexo=int(input("Ingrese su sexo, utilice 1 para femenino y 2 para masculino: "))
estadoCivil=int(input("Ingrese su estado civil, utilice 1 para soltero, 2 para casado y 3 para otro: "))
if(edad<=18 and sexo==1):
    print("Su edad es: " , edad)
    print("Su nombre es: " , nombre)
elif(estadoCivil==1):
    estadoCivil="Soltero"
    print("Su estado civil es: " , estadoCivil)
elif(estadoCivil==2):
    estadoCivil="Casado"
    print("Su estado civil es: " , estadoCivil)
elif(estadoCivil==3):
    estadoCivil="Otro"
    print("Su estado civil es: " , estadoCivil)