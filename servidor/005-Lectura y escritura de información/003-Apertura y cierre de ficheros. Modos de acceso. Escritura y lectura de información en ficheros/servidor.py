import datetime
import json
"""
    Programa de mensajería
    Parte de servidor
"""

# Declaración de variables

nombre_programa = "linesUp"
version = 0.01
AUTOR = "Jose Vicente Carratalá"

registros = open("registros.csv",'a')
archivomensajes = "mensajes.json"

# Clase auxiliar
class UtilidadesFechas:
    """
        Librería para almacenar
        utilidades en el manejo de fechas
    """
    @staticmethod
    def amdhms():
        """
            Crea una cadena numérica
            En el formato YYYYMMDDHHMMSS
        """
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
    """
        Clase para almacenar los mensajes
        Del sistema de mensajería
    """
    def __init__(self,texto_mensaje,marca_tiempo,mi_origen,mi_destino):
        self.__mensaje = texto_mensaje
        self.__tiempo = marca_tiempo
        self.__origen = mi_origen
        self.__destino = mi_destino
    def getMensaje(self):
        """
            Devuelve el mensaje
        """
        return self.__tiempo,self.__mensaje,self.__origen,self.__destino
    def __del__(self):
        return "Objeto destruido"

class MensajeEncriptado(Mensaje):
    def __init__(self, texto_mensaje, marca_tiempo, mi_origen, mi_destino, clave):
        super().__init__(texto_mensaje, marca_tiempo, mi_origen, mi_destino)
        self.__clave = clave
        self.__mensaje_encriptado = self.__encriptar_mensaje(texto_mensaje)
        
    def __encriptar_mensaje(self, mensaje):
        mensaje_encriptado = ''.join(
            chr((ord(char) + self.__clave - 32) % 95 + 32) for char in mensaje)
        return mensaje_encriptado
        
    def __desencriptar_mensaje(self, mensaje_encriptado):
        mensaje_desencriptado = ''.join(
            chr((ord(char) - self.__clave - 32) % 95 + 32) for char in mensaje_encriptado)
        return mensaje_desencriptado
        
    def getMensajeEncriptado(self):
        return self.__tiempo, self.__mensaje_encriptado, self.__origen, self.__destino
        
    def getMensajeDesencriptado(self):
        mensaje_desencriptado = self.__desencriptar_mensaje(self.__mensaje_encriptado)
        return self.__tiempo, mensaje_desencriptado, self.__origen, self.__destino

# Mensaje de bienvenida
if __name__ == "__main__":
    print("Bienvenidos a "+nombre_programa+", versión "+str(version)+", por "+AUTOR)
    clave = 3
    marca_de_tiempo = UtilidadesFechas.amdhms()
    assert len(str(marca_de_tiempo)) == 14, "La marca de tiempo generada no tiene el formato correcto."
    registros.write(str(UtilidadesFechas.amdhms())+"\n")
    registros.close()
    while True:
        try:
            mi_mensaje = input("Introduce el mensaje: ")
            mensajes = MensajeEncriptado(mi_mensaje,marca_de_tiempo,"Jose Vicente","Vicente",clave)
            print(mensajes.getMensaje())
            archivo_json_mensajes = open(archivomensajes,'r')
            datos = json.load(archivo_json_mensajes)
            datos.append(mensajes.getMensaje())
            archivo_json_mensajes.close()
            archivo_json_mensajes = open(archivomensajes,'w')
            json.dump(datos,archivo_json_mensajes,indent=4)
            archivo_json_mensajes.close()
        except Exception as e:
            print(f"ha ocurrido algún error: {e}")
        
    del mensajes

