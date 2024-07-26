import datetime
"""
    Programa de mensajería
    Parte de servidor
"""

# Declaración de variables

nombre_programa = "linesUp"
version = 0.01
AUTOR = "Jose Vicente Carratalá"

# Clase auxiliar
class UtilidadesFechas:
    @staticmethod
    def amdhms():
        fecha = datetime.datetime.now()
        año = str(fecha.year)
        mes = str(fecha.month).zfill(2)
        dia = str(fecha.day).zfill(2)
        hora = str(fecha.hour).zfill(2)
        minuto = str(fecha.minute).zfill(2)
        segundo = str(fecha.second).zfill(2)
        return int(año+mes+dia+hora+minuto+segundo)
    
# Clase mensaje
class Mensaje:
    def setMensaje(self,mensaje):
        self.mensaje = mensaje
    def getMensaje(self):
        return self.mensaje

# Mensaje de bienvenida

print("Bienvenidos a "+nombre_programa+", versión "+str(version)+", por "+AUTOR)

marca_de_tiempo = UtilidadesFechas.amdhms()
print(marca_de_tiempo)

mensajes = Mensaje()
mensajes.setMensaje("este es el primer mensaje")
print(mensajes.getMensaje())
