class SaleDetailModel:
    def __init__(self, mySQL):
        self.mySQL = mySQL
        
    def getSaleDetails(self):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM saleDetails')
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSaleDetail(self, SaleDetailId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute(
                'SELECT * FROM saleDetails WHERE SaleDetailId = %s', (SaleDetailId,))
            self.mySQL.connection.commit()
            return cur.fetchone()
        except Exception as e:
            print('ERROR:\n',e)
            
    def addSaleDetail(self, newSaleDetail):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('INSERT INTO saleDetails (saleId, productId, quantity, unitPrice, subtotal) VALUES (%s, %s, %s, %s, %s)',
                        (newSaleDetail['saleId'], newSaleDetail['productId'], newSaleDetail['quantity'], newSaleDetail['unitPrice'], newSaleDetail['subtotal'],))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n', e)
            
    def updateSaleDetail(self, SaleDetailId, updatedSaleDetail):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('UPDATE saleDetails SET saleId = %s, productId = %s, quantity = %s, unitPrice = %s, subtotal = %s WHERE SaleDetailId = %s',
                        (updatedSaleDetail['saleId'], updatedSaleDetail['productId'], updatedSaleDetail['quantity'], updatedSaleDetail['unitPrice'], updatedSaleDetail['subtotal'], SaleDetailId,))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def deleteSaleDetail(self, SaleDetailId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute(
                'DELETE FROM saleDetails WHERE SaleDetailId = %s', (SaleDetailId,))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getsaleDetailsBySale(self, saleId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute(
                'SELECT * FROM saleDetails WHERE saleId = %s', (saleId,))
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getsaleDetailsByProduct(self, productId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute(
                'SELECT * FROM saleDetails WHERE productId = %s', (productId,))
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getSaleDetailsByDate(self, date):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM saleDetails WHERE date = %s', (date,))
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            