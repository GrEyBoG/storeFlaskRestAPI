from flask import request, jsonify, Blueprint
from models.sales_model import SaleModel

saleController = Blueprint('saleController', __name__)

def initSaleController(app, mySQL):
    global SaleModel
    SaleModel = SaleModel(mySQL)
    
    app.register_blueprint(saleController)
    
def getSales():
    try:
        return jsonify(SaleModel.getSales())
    except Exception as e:
        return jsonify({'message': 'Sales Cant be Fetched'})
        print(e)

def getSale(saleId):
    try:
        return jsonify(SaleModel.getSale(saleId))
    except Exception as e:
        return jsonify({'message': 'Sale Cant be Fetched'})
        print(e)

def addSale():
    try:
        newSale = {
            'idProduct': request.json['idProduct'],
            'idClient': request.json['idClient'],
            'amount': request.json['amount'],
            'saleDate': request.json['saleDate']
        }
        SaleModel.addSale(newSale)
        return jsonify({'message': 'Sale Added Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Sale Cant be Added'})
        print(e)
        
def updateSale(saleId):
    try:
        updatedSale = {
            'idClient': request.json['idClient'],
            'idProduct': request.json['idProduct'],
            'amount': request.json['amount'],
            'saleDate': request.json['saleDate']
        }
        SaleModel.updateSale(saleId, updatedSale)  
        return jsonify({'message': 'Sale Updated Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Sale Cant be Updated'})
        print(e)
        
def deleteSale(saleId):
    try:
        SaleModel.deleteSale(saleId)
        return jsonify({'message': 'Sale Deleted Succesfully'})
    except Exception as e:
        print(e)

def getSalesByClient(idClient):
    try:
        return jsonify(SaleModel.getSalesByClient(idClient))
    except Exception as e:
        return jsonify({'message': 'Sales Cant be Fetched'})
        print(e)
        
def getSalesByProduct(idProduct):
    try:
        return jsonify(SaleModel.getSalesByProduct(idProduct))
    except Exception as e:
        print(e)

def getSalesByDate(saleDate):
    try:
        return jsonify(SaleModel.getSalesByDate(saleDate))
    except Exception as e:
        print(e)
        
def getSalesByClientAndProduct(idClient, idProduct):
    try:
        return jsonify(SaleModel.getSalesByClientAndProduct(idClient, idProduct))
    except Exception as e:
        print(e)
        
def getSalesByClientAndDate(idClient, saleDate):
    try:
        return jsonify(SaleModel.getSalesByClientAndDate(idClient, saleDate))
    except Exception as e:
        print(e)
        
def getSalesByProductAndDate(idProduct, saleDate):
    try:
        return jsonify(SaleModel.getSalesByProductAndDate(idProduct, saleDate))
    except Exception as e:
        print(e)

def getSalesByClientAndProductAndDate(idClient, idProduct, saleDate):
    try:
        return jsonify(SaleModel.getSalesByClientAndProductAndDate(idClient, idProduct, saleDate))
    except Exception as e:
        print(e)
        
def getSalesByAmount(amount):
    try:
        return jsonify(SaleModel.getSalesByAmount(amount))
    except Exception as e:
        print(e)