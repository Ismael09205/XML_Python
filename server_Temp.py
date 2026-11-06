from xmlrpc.server import SimpleXMLRPCServer
def fahre_to_cel (temp):
    celcius=((temp-32))/1.8
    return celcius
def cel_to_fahre (temp):
    fahren=((temp*1.8))+32
    return fahren

servidor = SimpleXMLRPCServer(("localhost", 8000))

servidor.register_function(fahre_to_cel, "celcius")
servidor.register_function(cel_to_fahre,"fahre")


print("Alzado el servidor .....")

servidor.serve_forever()
