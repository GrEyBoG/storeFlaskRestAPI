from flask import Flask
from flask_cors import CORS
from database.db import init_database
from routes.routs import routes
from controllers.products_controller import initProductController
from controllers.clients_controller import initClientController
from controllers.sales_controller import initSaleController

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes)

mySQL = init_database(app)
initProductController(app, mySQL)
initClientController(app, mySQL)
initSaleController(app, mySQL)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
