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
            cur.execute('SELECT * FROM products WHERE productId = %s', (productId,))
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
            
    def getProductByType(self, softwareType):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM products WHERE softwareType = %s', (softwareType,))
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def addProduct(self, newProduct):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('INSERT INTO products (name, description, price, softwareType, platform, releaseDate,availability) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                        (newProduct['name'], newProduct['description'], newProduct['price'], newProduct['softwareType'], newProduct['platform'], newProduct['releaseDate'], newProduct['availability'],))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def updateProduct(self, productId, updatedProduct):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('UPDATE products SET name = %s, description = %s, price = %s, softwareType = %s, platform = %s, releaseDate = %s, availability = %s WHERE id = %s',
                        (updatedProduct['name'], updatedProduct['description'], updatedProduct['price'], updatedProduct['softwareType'], updatedProduct['platform'], updatedProduct['releaseDate'], updatedProduct['availability'], productId,))
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
            
    def getPlatforms(self):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT DISTINCT platform FROM products')
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSoftwareTypes(self):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT DISTINCT softwareType FROM products')
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    
            
            
    
    