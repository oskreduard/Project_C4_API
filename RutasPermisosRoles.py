import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_security


@app.route("/permisos-roles",methods=['GET'])
def getPermisosRoles():
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permisos-roles'                        #Change the URL
    response = requests.get(url, headers=headers)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permisos-roles/rol/<string:id_rol>/permiso/<string:id_permiso>",methods=['POST'])
def crearPermisosRoles(id_rol,id_permiso):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permisos-roles/rol/'+id_rol+'/permiso/'+id_permiso                     #Change the URL
    response = requests.post(url, headers=headers)     #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permisos-roles/<string:id>",methods=['GET'])
def getPermisoRol(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permisos-roles/'+id                   #Change the URL
    response = requests.get(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permisos-roles/<string:id>/rol/<string:id_rol>/permiso/<string:id_permiso>", methods=['PUT'])
def modificarPermisoRol(id,id_rol, id_permiso):
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    url = url_backend_security + '/permisos-roles/' + id + '/rol/' + id_rol + '/permiso/' + id_permiso  # Change the URL
    response = requests.put(url, headers=headers)  # Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permisos-roles/<string:id>",methods=['DELETE'])
def deletePermisoRol(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permisos-roles/'+id                   #Change the URL
    response = requests.delete(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

