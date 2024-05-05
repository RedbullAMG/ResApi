from flask import Blueprint, jsonify, request
import uuid

#
from models.entities.Herr import Herr

# Models
from models.HerrModel import HerrModel

main=Blueprint('herr_blueprint',__name__)

@main.route('/')
def get_herrms():
    try:
        herrms=HerrModel.get_herrms()
        return jsonify(herrms)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/<id>')
def get_herr(id):
    try:
        herr=HerrModel.get_herr(id)
        if herr != None:
            return jsonify(herr)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
    
@main.route('/add',methods=['POST'])
def add_herr():
    try:
        nombre = request.json['nombre']
        precio = int(request.json['precio'])
        id = uuid.uuid4()
        herr=Herr(str(id), nombre, precio)
        
        affected_rows=HerrModel.add_herr(herr)
        
        if affected_rows == 1:
            return jsonify(herr.id)
        else:
            return jsonify({'message': "Error on insert"}),500
        
        
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
    
    
    
@main.route('/update/<id>',methods=['PUT'])
def update_herr(id):
    try:
        nombre = request.json['nombre']
        precio = int(request.json['precio'])
        herr = Herr (id, nombre, precio)
        
        affected_rows=HerrModel.update_herr(herr)
        
        if affected_rows == 1:
            return jsonify(herr.id)
        else:
            return jsonify({'message': "No herr updated"}),404
        
        
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
    
    
    
@main.route('/delete/<id>',methods=['DELETE'])
def delete_herr(id):
    try:
        herr=Herr(id)
        
        affected_rows = HerrModel.delete_herr(herr)
        
        if affected_rows == 1:
            return jsonify(herr.id)
        else:
            return jsonify({'message': "No Herr deleted"}),404
        
        
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500