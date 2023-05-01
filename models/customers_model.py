class CustomerModel:
    def __init__(self, mySQL):
        self.mySQL = mySQL
        
    def getCustomers(self):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM customers')
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getCustomer(self, customerId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM customers WHERE customerId = %s', (customerId,))
            self.mySQL.connection.commit()
            return cur.fetchone()
        except Exception as e:
            print('ERROR:\n',e)
            
    def addCustomer(self, newCustomer):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('INSERT INTO customers (email, password, firstName, lastName, address, phoneNumber) VALUES (%s, %s, %s, %s, %s, %s)',
                        (newCustomer['email'], newCustomer['password'], newCustomer['firstName'], newCustomer['lastName'], newCustomer['address'], newCustomer['phoneNumber'],))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n', e)

            
    def updateCustomer(self, customerId, updatedCustomer):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('UPDATE customers SET email = %s, password = %s, firstName = %s, lastName = %s, address = %s, phoneNumber = %s WHERE customerId = %s',
                        (updatedCustomer['email'], updatedCustomer['password'], updatedCustomer['firstName'], updatedCustomer['lastName'], updatedCustomer['address'], updatedCustomer['phoneNumber'], customerId,))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def deleteCustomer(self, customerId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('DELETE FROM customers WHERE customerId = %s', (customerId,))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getCustomerByEmail(self, email):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM customers WHERE email = %s', (email,))
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
            

