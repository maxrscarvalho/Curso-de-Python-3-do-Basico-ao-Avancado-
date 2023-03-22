'''
Method vs @classmethod vs #staticmethod
method  - self, metodo de instancia
@classmethod - cls, metodo de classe
@staticmethod - metodo estatico (Xself, Xcls)'''


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls, user, password):
        Connection = cls()
        Connection.user = user
        Connection.password = password
        return Connection

    @staticmethod
    def log(msg):
        print('LOG', msg)

# c1 = Connection()
c1 = Connection.create_with_auth('Max','1234')
# c1.set_user('max')
# c1.set_password('123')
print(Connection.log('Essa e a mensagem de Log'))
print(c1.user)
print(c1.password)