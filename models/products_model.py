class ProductModel:
    def __init__(self, mySQL):
        self.mySQL = mySQL
        
    def getProducts(self):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM products')
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getProduct(self, productId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM products WHERE id = %s', (productId,))
            self.mySQL.connection.commit()
            return cur.fetchone()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getProductByName(self, productName):
        try:
            cur = self.mySQL.connection.cursor()
            search_pattern = f'%{productName}%'
            cur.execute('SELECT * FROM products WHERE name LIKE %s', (search_pattern,))
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
        
    def addProduct(self, newProduct):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('INSERT INTO products (name, price, amount) VALUES (%s, %s, %s)', (newProduct['name'], newProduct['price'], newProduct['amount']))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
    
    def updateProduct(self, productId, updatedProduct):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('UPDATE products SET name = %s, price = %s, amount = %s WHERE id = %s',
                        (updatedProduct['name'], updatedProduct['price'], updatedProduct['amount'], productId))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def deleteProduct(self, productId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('DELETE FROM products WHERE id = %s', (productId,))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
            