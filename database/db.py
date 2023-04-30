from flask_mysqldb import MySQL

def init_database(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '12345678'
    app.config['MYSQL_DB'] = 'store'
    return MySQL(app)
