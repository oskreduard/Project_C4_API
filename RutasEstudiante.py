import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_academic


@app.route("/estudiantes",methods=['GET'])
def getEstudiantes():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_academic + '/estudiantes'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_academic + '/estudiantes'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_academic + '/estudiantes/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_academic + '/estudiantes/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_academic + '/estudiantes/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

