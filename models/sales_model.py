class SaleModel():
    def __init__(self, mySQL):
        self.mySQL = mySQL
        
    def getSales(self):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales')
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSale(self, saleId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE id = %s', (saleId,))
            return cur.fetchone()
        except Exception as e:
            print('ERROR:\n',e)
            
    def addSale(self, newSale):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('INSERT INTO sales (idProduct, idClient, amount, saleDate) VALUES (%s, %s, %s, %s)', (newSale['idProduct'], newSale['idClient'], newSale['amount'], newSale['saleDate']))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
    
    def updateSale(self, saleId, updatedSale):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('UPDATE sales SET idProduct = %s, idClient = %s, amount = %s, saleDate = %s WHERE id = %s',
                        (updatedSale['idProduct'], updatedSale['idClient'], updatedSale['amount'], updatedSale['saleDate'], saleId))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
    
    def deleteSale(self, saleId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('DELETE FROM sales WHERE id = %s', (saleId,))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSalesByClient(self, idClient):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE idClient = %s', (idClient,))
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSalesByProduct(self, idProduct):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE idProduct = %s', (idProduct,))
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSalesByDate(self, saleDate):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE saleDate = %s', (saleDate,))
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSalesByClientAndProduct(self, idClient, idProduct):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE idClient = %s AND idProduct = %s', (idClient, idProduct))
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSalesByClientAndDate(self, idClient, saleDate):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE idClient = %s AND saleDate = %s', (idClient, saleDate))
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSalesByProductAndDate(self, idProduct, saleDate):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE idProduct = %s AND saleDate = %s', (idProduct, saleDate))
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSalesByClientAndProductAndDate(self, idClient, idProduct, saleDate):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE idClient = %s AND idProduct = %s AND saleDate = %s', (idClient, idProduct, saleDate))
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSalesByAmount(self, amount):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE amount = %s', (amount,))
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    