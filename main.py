from tinydb import TinyDB
import tinydb
import requests
db = TinyDB('db.json',indent=4)

url = "https://randomuser.me/api/"
response = requests.get(url)
data = response.json()
for user in data['results']:
    db.insert({'last_name': user['name']['last'], 'first_name': user['name']['first'], 'age': user['dob']['age'], 'gender': user['gender']})  
users = db.all()
for user in users:
    print(user)
db.remove(tinydb.where('first_name') == 'Aziz')