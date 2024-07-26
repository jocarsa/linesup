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
    def __init__(self,texto_mensaje,marca_tiempo):
        self.mensaje = texto_mensaje
        self.tiempo = marca_tiempo
    def getMensaje(self):
        return self.tiempo,self.mensaje

# Mensaje de bienvenida

print("Bienvenidos a "+nombre_programa+", versión "+str(version)+", por "+AUTOR)

marca_de_tiempo = UtilidadesFechas.amdhms()

mensajes = Mensaje("Este es el primer mensaje",marca_de_tiempo)
print(mensajes.getMensaje())
