class SaleModel:
    def __init__(self, mySQL):
        self.mySQL = mySQL
        
    def getSales(self):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales')
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSale(self, saleId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE saleId = %s', (saleId,))
            self.mySQL.connection.commit()
            return cur.fetchone()
        except Exception as e:
            print('ERROR:\n',e)
            
    def addSale(self, newSale):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('INSERT INTO sales (customerId, total) VALUES (%s, %s)',
                        (newSale['customerId'], newSale['total'],))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n', e)
            
    def updateSale(self, saleId, updatedSale):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('UPDATE sales SET customerId = %s, total = %s WHERE saleId = %s',
                        (updatedSale['customerId'], updatedSale['total'], saleId,))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def deleteSale(self, saleId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('DELETE FROM sales WHERE saleId = %s', (saleId,))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSalesByCustomer(self, customerId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE customerId = %s', (customerId,))
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSalesByDate(self, date):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM sales WHERE date = %s', (date,))
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    