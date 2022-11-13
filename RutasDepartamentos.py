import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_academic


@app.route("/departamentos",methods=['GET'])
def getDepartamentos():
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_academic + '/departamentos'                        #Change the URL
    response = requests.get(url, headers=headers)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/departamentos",methods=['POST'])
def crearDepartamento():
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_academic + '/departamentos'                        #Change the URL
    response = requests.post(url, headers=headers,json=data)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/departamentos/<string:id>",methods=['GET'])
def getDepartamento(id):
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_academic + '/departamentos/'+id                       #Change the URL
    response = requests.get(url, headers=headers,json=data)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/departamentos/<string:id>",methods=['PUT'])
def modificarDepartamento(id):
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_academic + '/departamentos/'+id                       #Change the URL
    response = requests.put(url, headers=headers,json=data)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/departamentos/<string:id>",methods=['DELETE'])
def eliminarDepartamento(id):
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_academic + '/departamentos/'+id                       #Change the URL
    response = requests.delete(url, headers=headers,json=data)        #Change the Method
    json = response.json()
    return jsonify(json)

