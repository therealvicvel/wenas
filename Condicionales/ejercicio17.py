#17.	El IMSS requiere clasificar a las personas que se jubilaran en el año de 1997. Existen tres tipos de jubilaciones: por edad, por antigüedad joven y por antigüedad adulta. Las personas adscritas a la jubilación por edad deben tener 60 años o más y una antigüedad en su empleo de menos de 25 años.	Las personas adscritas a la jubilación por antigüedad joven deben tener menos de 60 años y una antigüedad en su empleo de 25 años o más. Las personas adscritas a la jubilación por antigüedad adulta deben tener 60 años o más y una antigüedad en su empleo de 25 años o más.
edad=0
joven=0
empleo=0
adulta=0
edad= int(input("Digite su edad: "))
empleo= int(input("Escriba los años que trabajó en su empleo:  "))
if edad <=60 and empleo>25:
    print("Usted está adscrito a jubilación por edad. ")
elif edad>60 and empleo<=25:
    print("Usted se encuentra adscrito a jubilación por antiguedad joven. ")
elif edad <=60 and empleo<=25:
    print("Usted se encuentra adscrito a jubilacion por antiguedad adulta.")