n1=int(input("Imgrese primer número: "))
n2=int(input("Imgrese segundo número: "))
oper=input("Ingrese operador[+,-,*,/]")

if oper=="+":
    print("La suma es:",n1+n2)
elif oper=="-":
    print("La resta es:",n1-n2)
elif oper=="*":
    print("La multiplicasión es:",n1*n2)
elif oper=="/":
    print("La división es:",n1/n2)

else:
    print("Operador desconosido")