from admin import Admin
from database import DataBase

a = Admin('rolf', '1234', 3)

a.save()
print(DataBase.find(lambda x: x['username'] == 'rolf'))