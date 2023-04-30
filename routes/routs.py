from flask import Blueprint
from controllers.products_controller import getProducts, addProduct, getProductByName, updateProduct, deleteProduct
from controllers.clients_controller import getClients, addClient, getClient, updateClient, deleteClient, getClientByEmail
from controllers.sales_controller import getSales, addSale, getSale, updateSale, deleteSale, getSalesByClient, getSalesByProduct, getSalesByDate, getSalesByClientAndProduct, getSalesByClientAndDate, getSalesByProductAndDate, getSalesByClientAndProductAndDate, getSalesByAmount

routes = Blueprint('routes', __name__)

# PRODUCTS
routes.route('/getProducts', methods=['GET'])(getProducts)
routes.route('/getProduct/<int:productId>', methods=['GET'])(getProductByName)
routes.route('/addProduct', methods=['POST'])(addProduct)
routes.route('/updateProduct/<int:productId>', methods=['PUT'])(updateProduct)
routes.route('/deleteProduct/<int:productId>', methods=['DELETE'])(deleteProduct)
routes.route('/getProductByName/<string:productName>', methods=['GET'])(getProductByName)

# CLIENTS
routes.route('/getClients', methods=['GET'])(getClients)
routes.route('/getClient/<int:clientId>', methods=['GET'])(getClient)
routes.route('/addClient', methods=['POST'])(addClient)
routes.route('/updateClient/<int:clientId>', methods=['PUT'])(updateClient)
routes.route('/deleteClient/<int:clientId>', methods=['DELETE'])(deleteClient)
routes.route('/getClientByEmail/<string:clientEmail>', methods=['GET'])(getClientByEmail)

# SALES
routes.route('/getSales', methods=['GET'])(getSales)
routes.route('/getSale/<int:saleId>', methods=['GET'])(getSale)
routes.route('/addSale', methods=['POST'])(addSale)
routes.route('/updateSale/<int:saleId>', methods=['PUT'])(updateSale)
routes.route('/deleteSale/<int:saleId>', methods=['DELETE'])(deleteSale)
routes.route('/getSalesByClient/<int:idClient>', methods=['GET'])(getSalesByClient)
routes.route('/getSalesByProduct/<int:idProduct>', methods=['GET'])(getSalesByProduct)
routes.route('/getSalesByDate/<string:saleDate>', methods=['GET'])(getSalesByDate)
routes.route('/getSalesByClientAndProduct/<int:idClient>/<int:idProduct>', methods=['GET'])(getSalesByClientAndProduct)
routes.route('/getSalesByClientAndDate/<int:idClient>/<string:saleDate>', methods=['GET'])(getSalesByClientAndDate)
routes.route('/getSalesByProductAndDate/<int:idProduct>/<string:saleDate>', methods=['GET'])(getSalesByProductAndDate)
routes.route('/getSalesByClientAndProductAndDate/<int:idClient>/<int:idProduct>/<string:saleDate>', methods=['GET'])(getSalesByClientAndProductAndDate)
routes.route('/getSalesByAmount/<float:amount>', methods=['GET'])(getSalesByAmount)