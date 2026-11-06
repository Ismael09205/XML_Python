#172.31.116.80
import socket
socketCliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketCliente.connect(("localhost",5000))
while True:
    print("Envio de mensajes")
    print("Ingrese cero si quiere salir :D")

    mensaje=input("Ingrese su mensaje: ")
    if mensaje=="0":
        print ("Saliendo.....")
        
        break
       
    
    socketCliente.send(mensaje.encode())
    respuesta=socketCliente.recv(1024)
    print("Respuesta: ",respuesta.decode())
socketCliente.close()    