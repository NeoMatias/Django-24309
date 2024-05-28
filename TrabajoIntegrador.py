#TRABAJO INTEGRADOR 

#PUNTO 1 (funcion que calcula maximo comun divisor entre dos numeros)

def cuenta(x,y):
    while y:
        x,y=y,x%y
    return x

num1=35
num2=98
print(f"el maximo comun divisor de {num1}y{num2} es{cuenta(num1,num2)}")
 
#PUNTO 2 (funcion que calcule el minimo comun multiplo entre dos numeros)

