n1=int(input("Ingrese primer número: "))
n2=int(input("Ingrese segundo número: "))
oper=input("Ingrese operador[+,*]")

if oper=="+":
    print("La suma es:",n1+n2)
elif oper=="*":
    print("La multiplicasión es:",n1*n2)  
else:
    print("Operador desconocido")  