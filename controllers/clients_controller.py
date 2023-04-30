from flask import request, jsonify, Blueprint
from models.clients_model import ClientModel

clientController = Blueprint('clientController', __name__)

def initClientController(app, mySQL):
    global ClientModel
    ClientModel = ClientModel(mySQL)
    
    app.register_blueprint(clientController)
    
def getClients():
    try:
        return jsonify(ClientModel.getClients())
    except Exception as e:
        return jsonify({'message': 'Clients Cant be Fetched'})
        print(e)
        
def getClient(clientId):
    try:
        return jsonify(ClientModel.getClient(clientId))
    except Exception as e:
        return jsonify({'message': 'Client Cant be Fetched'})
        print(e)
        
def addClient():
    try:
        newClient = {
            'name': request.json['name'],
            'lastName': request.json['lastName'],
            'age': request.json['age'],
            'email': request.json['email'],
        }
        ClientModel.addClient(newClient)
        return jsonify({'message': 'Client Added Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Client Cant be Added'})
        print(e)
        
def updateClient(clientId):
    try:
        updatedClient = {
            'name': request.json['name'],
            'lastName': request.json['lastName'],
            'age': request.json['age'],
            'email': request.json['email']
        }
        ClientModel.updateClient(clientId, updatedClient)
        return jsonify({'message': 'Client Updated Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Client Cant be Updated'})
        print(e)
        
def deleteClient(clientId):
    try:
        ClientModel.deleteClient(clientId)
        return jsonify({'message': 'Client Deleted Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Client Cant be Deleted'})
        print(e)
        
def getClientByEmail(clientEmail):
    try:
        return jsonify(ClientModel.getClientByEmail(clientEmail))
    except Exception as e:
        return jsonify({'message': 'Client Cant be Fetched'})
        print(e)