import xmlrpc.client
cliente=xmlrpc.client.ServerProxy("http://172.31.116.80:8000/")
n1=0
n2=0
def calculadora_opciones():
    global n1,n2
    print("---------------Menu Calculadora---------------------")
    opcion=input("Ingrese la opcion: ")
    
    if(opcion=="1"):
        n1=int(input("Ingrese el primer numero: "))
        n2=int(input("Ingrese el segundo numero: "))
        print(cliente.suma(n1,n2))
    if(opcion=="2"):
        n1=int(input("Ingrese el primer numero: "))
        n2=int(input("Ingrese el segundo numero: "))
        print(cliente.resta(n1,n2))
    if(opcion=="3"):
        n2=int(input("Ingrese el segundo numero: "))
        n1=int(input("Ingrese el primer numero: "))
        print(cliente.multiplicacion(n1,n2))
    if(opcion=="4"):
        n1=int(input("Ingrese el primer numero: "))
        n2=int(input("Ingrese el segundo numero: "))
        print(cliente.division(n1,n2))
calculadora_opciones()   
