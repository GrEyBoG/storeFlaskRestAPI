from flask import request, jsonify, Blueprint
from models.saleDetails_model import SaleDetailModel

SaleetailsController = Blueprint('SaleetailsController', __name__)

def initSaleDetailsController(app, mySQL):
    global SaleDetailModel
    SaleDetailModel = SaleDetailModel(mySQL)
    
    app.register_blueprint(SaleetailsController)
    
def getSaleDetails():
    try:
        return jsonify(SaleDetailModel.getSaleDetails())
    except Exception as e:
        return jsonify({'message': 'Saleetails Cant be Fetched'})
        print(e)
        
def getSaleDetail(SaleetailId):
    try:
        return jsonify(SaleDetailModel.getSaleDetail(SaleetailId))
    except Exception as e:
        return jsonify({'message': 'Saleetail Cant be Fetched'})
        print(e)
        
def addSaleDetail():
    try:
        newSaleetail = {
            "saleId": request.json['saleId'],
            "productId": request.json['productId'],
            "quantity": int(request.json['quantity']),
            "unitPrice": float(request.json['unitPrice']),
            "subtotal": float(request.json['unitPrice']) * int(request.json['quantity'])
        }
        SaleDetailModel.addSaleDetail(newSaleetail)
        return jsonify({'message': 'Saleetail Added Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Saleetail Cant be Added'})
        print(e)
        
def updateSaleDetail(SaleetailId):
    try:
        updatedSaleetail = {
            "saleId": request.json['saleId'],
            "productId": request.json['productId'],
            "quantity": int(request.json['quantity']),
            "unitPrice": float(request.json['unitPrice']),
            "subtotal": float(request.json['unitPrice']) * int(request.json['quantity'])
        }
        SaleDetailModel.updateSaleDetail(SaleetailId, updatedSaleetail)
        return jsonify({'message': 'Saleetail Updated Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Saleetail Cant be Updated'})
        print(e)
        
def deleteSaleDetail(SaleetailId):
    try:
        SaleDetailModel.deleteSaleDetail(SaleetailId)
        return jsonify({'message': 'Saleetail Deleted Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Saleetail Cant be Deleted'})
        print(e)
        
def getSaleDetailsBySale(saleId):
    try:
        return jsonify(SaleDetailModel.getSaleDetailsBySale(saleId))
    except Exception as e:
        return jsonify({'message': 'Saleetails Cant be Fetched'})
        print(e)
        
def getSaleDetailsByProduct(productId):
    try:
        return jsonify(SaleDetailModel.getSaleDetailsByProduct(productId))
    except Exception as e:
        return jsonify({'message': 'Saleetails Cant be Fetched'})
        print(e)
        

def getSaleDetailsByDate(date):
    try:
        return jsonify(SaleDetailModel.getSaleDetailsByDate(date))
    except Exception as e:
        return jsonify({'message': 'Saleetails Cant be Fetched'})
        print(e)


