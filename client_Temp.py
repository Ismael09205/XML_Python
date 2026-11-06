import xmlrpc.client
cliente=xmlrpc.client.ServerProxy("http://172.31.116.80:8000/")
n1=0
n2=0
while True:
    
        print("---------------Calcular Temperatura---------------------")
        print("1. Pasar de Fahrenheit a Celcius")
        print("2. Pasar de Celcius a Fahrenheit ")

        opcion=input("Ingrese la opcion: ")
        
        if(opcion=="1"):
            n1=int(input("Ingrese la temperatura: "))
            print(cliente.farCel(n1))
        if(opcion=="2"):
            n1=int(input("Ingrese la temperatura: "))
            print(cliente.celFar(n1))
        if(opcion=="0"):
            print("Saliendo....")   
            break
