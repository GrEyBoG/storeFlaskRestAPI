from flask import request, jsonify, Blueprint
from models.products_model import ProductModel

productController = Blueprint('productController', __name__)

def initProductController(app, mySQL):
    global ProductModel
    ProductModel = ProductModel(mySQL)
    
    app.register_blueprint(productController)
    
def getProducts():
    try:
        return jsonify(ProductModel.getProducts())
    except Exception as e:
        return jsonify({'message': 'Products Cant be Fetched'})
        print(e)
        
def getProduct(productId):
    try:
        return jsonify(ProductModel.getProduct(productId))
    except Exception as e:
        return jsonify({'message': 'Product Cant be Fetched'})
        print(e)
        
def getProductByName(productName):
    try:
        return jsonify(ProductModel.getProductByName(productName))
    except Exception as e:
        return jsonify({'message': 'Product Cant be Fetched'})
        print(e)

def addProduct():
    try:
        newProduct = {
            'name': request.json['name'],
            'price': request.json['price'],
            'amount': request.json['amount']
        }
        ProductModel.addProduct(newProduct)
        return jsonify({'message': 'Product Added Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Product Cant be Added'})
        print(e)

def updateProduct(productId):
    try:
        updatedProduct = {
            'name': request.json['name'],
            'price': request.json['price'],
            'amount': request.json['amount']
        }
        ProductModel.updateProduct(productId, updatedProduct)
        return jsonify({'message': 'Product Updated Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Product Cant be Updated'})
        print(e)

def deleteProduct(productId):
    try:
        ProductModel.deleteProduct(productId)
        return jsonify({'message': 'Product Deleted Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Product Cant be Deleted'})
        print(e)

