nombreEmpleado=""
salarioHora=0
valorRetencion=0
salarioNeto=0
horasTrabajadas=0
salarioBruto=0
nombreEmpleado=input("Señor empleado, por favor ingrese su nombre: ")
salarioHora=int(input("Ingrese su salario por hora: "))
horasTrabajadas=int(input("Ingrese las horas trabajadas: "))
salarioBruto=salarioHora*horasTrabajadas
if(salarioBruto<=250500):
    salarioNeto=salarioBruto
    print("Su nombre es: " , nombreEmpleado)
    print("Su salario bruto es: " , salarioBruto)
    print("Su salario neto es: " , salarioNeto)
    print("Como su salario es inferior a 250500, usted no tiene retención. ")
elif(salarioBruto>=250501 and salarioBruto<=300000):
    valorRetencion=0.05
    salarioNeto=salarioBruto-(salarioBruto*valorRetencion)
    print("Su nombre es: " , nombreEmpleado)
    print("Su salario bruto es: " , salarioBruto)
    print("El valor de la retención es: " , (valorRetencion*salarioBruto))
    print("Su salario neto es: " , salarioNeto)
elif(salarioBruto>300000):
    valorRetencion=0.08
    salarioNeto=salarioBruto-(salarioBruto*valorRetencion)
    print("Su nombre es: " , nombreEmpleado)
    print("Su salario bruto es: " , salarioBruto)
    print("El valor de la retención es: " , (valorRetencion*salarioBruto))
    print("Su salario neto es: " , salarioNeto)