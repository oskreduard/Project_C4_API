import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_academic

@app.route("/inscripciones",methods=['GET'])
def getinscripciones():
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_academic + '/inscripciones'                        #Change the URL
    response = requests.get(url, headers=headers)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_estudiante,id_materia):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    print("Entra a crear un inscipcion")
    url = url_backend_academic + '/inscripciones/estudiante/'+id_estudiante+'/materia/'+id_materia  # Change the URL
    print(url)
    response = requests.post(url, headers=headers ,json=data)  # Change the Method
    print(response)
    json = response.json()
    print(json)
    return jsonify(json)

@app.route("/inscripciones/<string:id>",methods=['GET'])
def getInscripcion(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    url = url_backend_academic + '/inscripciones/'+id  # Change the URL
    response = requests.get(url, headers=headers)  # Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['PUT'])
def modificarInscripcion(id_inscripcion,id_estudiante,id_materia):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    url = url_backend_academic + '/inscripciones/' + id_inscripcion + '/estudiante/' + id_estudiante + '/materia/' + id_materia  # Change the URL
    response = requests.put(url, headers=headers,json=data)  # Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/inscripciones/<string:id>",methods=['DELETE'])
def eliminarInscripcion(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    url = url_backend_academic + '/inscripciones/' + id  # Change the URL
    response = requests.delete(url, headers=headers)  # Change the Method
    json = response.json()
    return jsonify(json)
