"""
    Programa de mensajería
    Parte de servidor
"""

# Declaración de variables

nombre_programa = "linesUp"
version = 0.01
AUTOR = "Jose Vicente Carratalá"

# Clase mensaje
class Mensaje:
    def setMensaje(self,mensaje):
        self.mensaje = mensaje
    def getMensaje(self):
        return self.mensaje

# Mensaje de bienvenida

print("Bienvenidos a "+nombre_programa+", versión "+str(version)+", por "+AUTOR)

mensajes = Mensaje()
mensajes.setMensaje("este es el primer mensaje")
print(mensajes.getMensaje())
