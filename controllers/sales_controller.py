from flask import request, jsonify, Blueprint
from models.sales_model import SaleModel

salesController = Blueprint('salesController', __name__)

def initSalesController(app, mySQL):
    global SaleModel
    SaleModel = SaleModel(mySQL)
    
    app.register_blueprint(salesController)
    
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
            "customerId": request.json['customerId'],
            "total": request.json['total'],
        }
        SaleModel.addSale(newSale)
        return jsonify({'message': 'Sale Added Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Sale Cant be Added'})
        print(e)

def updateSale(saleId):
    try:
        updatedSale = {
            "customerId": request.json['customerId'],
            "total": request.json['total'],
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
        return jsonify({'message': 'Sale Cant be Deleted'})
        print(e)

def getSalesByCustomer(customerId):
    try:
        return jsonify(SaleModel.getSaleByCustomer(customerId))
    except Exception as e:
        return jsonify({'message': 'Sale Cant be Fetched'})
        print(e)

def getSalesByDate(date):
    try:
        return jsonify(SaleModel.getSaleByDate(date))
    except Exception as e:
        return jsonify({'message': 'Sale Cant be Fetched'})
        print(e)