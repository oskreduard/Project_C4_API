import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_academic


@app.route("/materias",methods=['GET'])
def getMaterias():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_academic + '/materias'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/materias",methods=['POST'])
def crearMateria():
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_academic + '/materias'                        #Change the URL
    response = requests.post(url, headers=headers,json=data)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/materias/<string:id>",methods=['GET'])
def getMateria(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_academic + '/materias/'+id                   #Change the URL
    response = requests.get(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/materias/<string:id>",methods=['PUT'])
def modificarMateria(id):
    data = request.get_json()  # BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    url = url_backend_academic + '/materias/'+id      # Change the URL
    response = requests.put(url, headers=headers, json=data)  # Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/materias/<string:id>",methods=['DELETE'])
def eliminarMateria(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_academic + '/materias/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/materias/<string:id>/departamento/<string:id_departamento>",methods=['PUT'])
def asignarDepartamentoAMateria(id,id_departamento):
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    url = url_backend_academic + '/materias/'+id+'/departamento/'+ id_departamento  # Change the URL
    response = requests.put(url, headers=headers)  # Change the Method
    json = response.json()
    return jsonify(json)