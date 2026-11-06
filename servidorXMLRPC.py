from xmlrpc.server import SimpleXMLRPCServer
def sumar (a,b):
    return a+b
def restar (a,b):
    return a-b
def multiplicar (a,b):
    return a*b
def dividir (a,b):
    if(b==0):
        return ("Imposible divisiones entre 0")
    return a/b
servidor = SimpleXMLRPCServer(("localhost", 8000))

servidor.register_function(sumar, "suma")
servidor.register_function(restar,"resta")
servidor.register_function(multiplicar,"multiplicacion")
servidor.register_function(dividir,"division")

print("Alzado el servidor .....")

servidor.serve_forever()
