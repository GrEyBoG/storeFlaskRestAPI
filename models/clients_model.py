class ClientModel():
    def __init__(self, mySQL):
        self.mySQL = mySQL
    
    def getClients(self):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM clients')
            self.mySQL.connection.commit()
            return cur.fetchall()
        except Exception as e:
            print('ERROR:\n',e)
    
    def getClient(self, clientId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM clients WHERE id = %s', (clientId,))
            self.mySQL.connection.commit()
            return cur.fetchone()
        except Exception as e:
            print('ERROR:\n',e)
            
    def getClientByEmail(self, email):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('SELECT * FROM clients WHERE email = %s', (email,))
            self.mySQL.connection.commit()
            return cur.fetchone()
        except Exception as e:
            print('ERROR:\n',e)
            
    def addClient(self, newClient):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('INSERT INTO clients (name, lastName, age, email) VALUES (%s, %s, %s, %s)', (newClient['name'], newClient['lastName'], newClient['age'], newClient['email']))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def updateClient(self, clientId, updatedClient):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('UPDATE clients SET name = %s, lastName = %s, age = %s, email = %s WHERE id = %s',
                        (updatedClient['name'], updatedClient['lastName'], updatedClient['age'], updatedClient['email'], clientId))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)
            
    def deleteClient(self, clientId):
        try:
            cur = self.mySQL.connection.cursor()
            cur.execute('DELETE FROM clients WHERE id = %s', (clientId,))
            self.mySQL.connection.commit()
        except Exception as e:
            print('ERROR:\n',e)