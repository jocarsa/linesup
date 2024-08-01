from flask import Flask, request, jsonify
from servidor import UtilidadesFechas, Mensaje, MensajeEncriptado
import json

app = Flask(__name__)

@app.route('/')
def raiz():
    return "Hola desde el servidor"

@app.route('/nuevomensaje')
def nuevoMensaje():
    origen = request.args.get('origen')
    destino = request.args.get('destino')
    mensaje = request.args.get('mensaje')
    marca_de_tiempo = UtilidadesFechas.amdhms()
    mensajes = MensajeEncriptado(mensaje,marca_de_tiempo,origen,destino,3)
    archivomensajes = "archivos/mensajes.json"
    archivo_json_mensajes = open(archivomensajes,'r')
    datos = json.load(archivo_json_mensajes)
    datos.append(mensajes.getMensaje())
    archivo_json_mensajes.close()
    archivo_json_mensajes = open(archivomensajes,'w')
    json.dump(datos,archivo_json_mensajes,indent=4)
    archivo_json_mensajes.close()
    return "{'resultado':'ok'}"

@app.route('/mensajes')
def mensajes():
    json_file_path = 'archivos/mensajes.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,port=3000)
