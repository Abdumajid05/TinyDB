from tinydb import TinyDB
import tinydb

db = TinyDB('db.json',indent=4)

data1 = {'first_name': 'Adham', 'last_name': 'Turopov', 'job': 'Software Engineer'}
data2 = {'first_name': 'Aziz', 'last_name': 'Aliyev', 'job': 'Project Manager'}

db.insert_multiple([data1, data2])

