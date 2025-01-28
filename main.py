from tinydb import TinyDB
import tinydb
import requests
db = TinyDB('phone.json',indent=4)

phones = [
    {"name": "Samsung Galaxy A25 8/256GB", "price": 3262500, "storage": "256GB", "camera": "50MP", "battery": "5000mAh"},
    {"name": "Samsung Galaxy S23 FE 8/128GB", "price": 5720000, "storage": "128GB", "camera": "50MP", "battery": "4500mAh"},
    {"name": "Samsung Galaxy S23 FE 8/256GB", "price": 6630000, "storage": "256GB", "camera": "50MP", "battery": "4500mAh"},
    {"name": "Samsung Galaxy Z Fold 6 12/512GB", "price": 19522500, "storage": "512GB", "camera": "50MP", "battery": "4800mAh"},
    {"name": "Samsung Galaxy A25 8/128GB", "price": 2878000, "storage": "128GB", "camera": "50MP", "battery": "5000mAh"},
    {"name": "Samsung Galaxy S24+ 12/512GB", "price": 12065000, "storage": "512GB", "camera": "50MP", "battery": "4900mAh"},
    {"name": "Infinix Note 40 Pro 12/256GB", "price": 3741000, "storage": "256GB", "camera": "108MP", "battery": "5000mAh"},
    {"name": "Apple iPhone 16 Pro Max 256GB", "price": 17139000, "storage": "256GB", "camera": "48MP", "battery": "4352mAh"},
    {"name": "Xiaomi Poco X5 Pro 12/512GB", "price": 4745000, "storage": "512GB", "camera": "108MP", "battery": "5000mAh"},
    {"name": "Tecno Spark 20 Pro 8/256GB", "price": 2389000, "storage": "256GB", "camera": "50MP", "battery": "5000mAh"},
    {"name": "Samsung Galaxy A25 6/128GB", "price": 2849000, "storage": "128GB", "camera": "50MP", "battery": "5000mAh"},
    {"name": "Samsung Galaxy A35 8/256GB", "price": 4017000, "storage": "256GB", "camera": "64MP", "battery": "5000mAh"},
    {"name": "Samsung Galaxy A16 6/128GB", "price": 2171000, "storage": "128GB", "camera": "50MP", "battery": "5000mAh"},
    {"name": "Xiaomi 14 12/512GB", "price": 4355000, "storage": "512GB", "camera": "50MP", "battery": "5000mAh"},
    {"name": "Xiaomi Poco X6 Pro 8/256GB", "price": 4225000, "storage": "256GB", "camera": "108MP", "battery": "5000mAh"}
]
db.insert_multiple(phones)