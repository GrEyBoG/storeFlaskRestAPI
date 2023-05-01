from flask import Flask
from flask_cors import CORS
from database.db import init_database
from routes.routs import routes
from controllers.products_controller import initProductController
from controllers.customers_controller import initCustomerController
from controllers.sales_controller import initSalesController
from controllers.saleDetails_controller import initSaleDetailsController

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes)

mySQL = init_database(app)
initProductController(app, mySQL)
initCustomerController(app, mySQL)
initSalesController(app, mySQL)
initSaleDetailsController(app, mySQL)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
