from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017")
db = client["userdata"]
collection = db["users"]

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    if name and email:
        collection.insert_one({'name': name, 'email': email})
        return 'Data inserted successfully!'
    else:
        return 'Invalid data!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
