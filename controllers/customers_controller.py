from flask import request, jsonify, Blueprint
from models.customers_model import CustomerModel

customerController = Blueprint('customerController', __name__)

def initCustomerController(app, mySQL):
    global CustomerModel
    CustomerModel = CustomerModel(mySQL)
    
    app.register_blueprint(customerController)
    
def getCustomers():
    try:
        return jsonify(CustomerModel.getCustomers())
    except Exception as e:
        return jsonify({'message': 'Customers Cant be Fetched'})
        print(e)

def getCustomer(customerId):
    try:
        return jsonify(CustomerModel.getCustomer(customerId))
    except Exception as e:
        return jsonify({'message': 'Customer Cant be Fetched'})
        print(e)
        

def addCustomer():
    try:
        newCustomer = {
            "email": request.json['email'],
            "password": request.json['password'],
            "firstName": request.json['firstName'],
            "lastName": request.json['lastName'],
            "address": request.json['address'],
            "phoneNumber": request.json['phoneNumber']
        }
        CustomerModel.addCustomer(newCustomer)
        return jsonify({'message': 'Customer Added Succesfully'})
    except Exception as e:
        print('newCustomer: ', e)
        return jsonify({'message': 'Customer Cant be Added'})

        
def updateCustomer(customerId):
    try:
        updatedCustomer = {
            "email": request.json['email'],
            "password": request.json['password'],
            "firstName": request.json['firstName'],
            "lastName": request.json['lastName'],
            "address": request.json['address'],
            "phoneNumber": request.json['phoneNumber']
        }
        CustomerModel.updateCustomer(customerId, updatedCustomer)
        return jsonify({'message': 'Customer Updated Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Customer Cant be Updated'})
        print(e)
        
def deleteCustomer(customerId):
    try:
        CustomerModel.deleteCustomer(customerId)
        return jsonify({'message': 'Customer Deleted Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Customer Cant be Deleted'})
        print(e)
        
def getCustomerByEmail(email):
    try:
        return jsonify(CustomerModel.getCustomerByEmail(email))
    except Exception as e:
        return jsonify({'message': 'Customer Cant be Fetched'})
        print(e)