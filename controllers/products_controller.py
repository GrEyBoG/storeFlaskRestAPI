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
        
def getProductByType(softwareType):
    try:
        return jsonify(ProductModel.getProductByType(softwareType))
    except Exception as e:
        return jsonify({'message': 'Product Cant be Fetched'})
        print(e)
        
def addProduct():
    try:
        newProduct = {
            "name": request.json['name'],
            "description": request.json['description'],
            "price": request.json['price'],
            "softwareType": request.json['softwareType'],
            "platform": request.json['platform'],
            "releaseDate": request.json['releaseDate'],
            "availability": request.json['availability']
        }
        ProductModel.addProduct(newProduct)
        return jsonify({'message': 'Product Added Succesfully'})
    except Exception as e:
        return jsonify({'message': 'Product Cant be Added'})
        print(e)
        
def updateProduct(productId):
    try:
        updatedProduct = {
            "name": request.json['name'],
            "description": request.json['description'],
            "price": request.json['price'],
            "softwareType": request.json['softwareType'],
            "platform": request.json['platform'],
            "releaseDate": request.json['releaseDate'],
            "availability": request.json['availability']
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
        print(e)

def getPlatforms():
    try:
        return jsonify(ProductModel.getPlatforms())
    except Exception as e:
        return jsonify({'message': 'Platforms Cant be Fetched'})
        print(e)
        
def getSoftwareTypes():
    try: 
        return jsonify(ProductModel.getSoftwareTypes())
    except Exception as e:
        return jsonify({'message': 'Software Types Cant be Fetched'})
        print(e)
        