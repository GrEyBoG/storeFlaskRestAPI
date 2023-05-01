from flask import Blueprint
from controllers.products_controller import getProducts, getProduct, getProductByName, getProductByType, addProduct, updateProduct, deleteProduct, getPlatforms, getSoftwareTypes
from controllers.customers_controller import getCustomers, getCustomer, addCustomer, updateCustomer, deleteCustomer, getCustomerByEmail
from controllers.sales_controller import getSales, getSale, addSale, updateSale, deleteSale, getSalesByCustomer, getSalesByDate
from controllers.saleDetails_controller import getSaleDetails, getSaleDetail, addSaleDetail, updateSaleDetail, deleteSaleDetail, getSaleDetailsBySale, getSaleDetailsByDate
 
routes = Blueprint('routes', __name__)

# PRODUCTS
routes.route('/getProducts', methods=['GET'])(getProducts)
routes.route('/getProduct/<int:productId>', methods=['GET'])(getProduct)
routes.route('/getProductByName/<string:productName>', methods=['GET'])(getProductByName)
routes.route('/getProductByType/<string:softwareType>', methods=['GET'])(getProductByType)
routes.route('/addProduct', methods=['POST'])(addProduct)
routes.route('/updateProduct/<int:productId>', methods=['PUT'])(updateProduct)
routes.route('/deleteProduct/<int:productId>', methods=['DELETE'])(deleteProduct)
routes.route('/getPlatforms', methods=['GET'])(getPlatforms)
routes.route('/getSoftwareTypes', methods=['GET'])(getSoftwareTypes)

# CUSTOMERS
routes.route('/getCustomers', methods=['GET'])(getCustomers)
routes.route('/getCustomer/<int:customerId>', methods=['GET'])(getCustomer)
routes.route('/getCustomerByEmail/<string:email>', methods=['GET'])(getCustomerByEmail)
routes.route('/addCustomer', methods=['POST'])(addCustomer)
routes.route('/updateCustomer/<int:customerId>', methods=['PUT'])(updateCustomer)
routes.route('/deleteCustomer/<int:customerId>', methods=['DELETE'])(deleteCustomer)
routes.route('/getCustomerByEmail/<string:email>', methods=['GET'])(getCustomerByEmail)

# SALES
routes.route('/getSales', methods=['GET'])(getSales)
routes.route('/getSale/<int:saleId>', methods=['GET'])(getSale)
routes.route('/addSale', methods=['POST'])(addSale)
routes.route('/updateSale/<int:saleId>', methods=['PUT'])(updateSale)
routes.route('/deleteSale/<int:saleId>', methods=['DELETE'])(deleteSale)
routes.route('/getSalesByCustomer/<int:customerId>', methods=['GET'])(getSalesByCustomer)
routes.route('/getSalesByDate/<string:date>', methods=['GET'])(getSalesByDate)

# SALE DETAILS
routes.route('/getSaleDetails', methods=['GET'])(getSaleDetails)
routes.route('/getSaleDetail/<int:SaleetailId>', methods=['GET'])(getSaleDetail)
routes.route('/addSaleDetail', methods=['POST'])(addSaleDetail)
routes.route('/updateSaleDetail/<int:SaleetailId>', methods=['PUT'])(updateSaleDetail)
routes.route('/deleteSaleDetail/<int:SaleetailId>', methods=['DELETE'])(deleteSaleDetail)
routes.route('/getSaleDetailsBySale/<int:saleId>', methods=['GET'])(getSaleDetailsBySale)
routes.route('/getSaleDetailsByDate/<string:date>', methods=['GET'])(getSaleDetailsByDate)

