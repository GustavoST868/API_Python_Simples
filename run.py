#modules and libraries
from flask import Flask, jsonify, request

app = Flask(__name__)

# example users
user = [
    {
        'id': 1,
        'user': 'Gustavo',
        'password': '12345'
    },
    {
        'id': 2,
        'user': 'Maria',
        'password': 'password123'
    },
    
]

#function to consult all users
@app.route('/users')
def getUsers():
    return jsonify(user)

#consult(id) user
@app.route('/users/<int:id>', methods=['GET'])
def getUsersId(id):
    for user_ in user:
        if user_.get('id') == id:
            return jsonify(user_)
        
#edit user
        @app.route('/users/<int:id>', methods=['PUT'])
        def edit(id):
            user_change = request.get_json()
            for index,user in enumerate(user):
                if user.get('id') == id:
                    user[index].update(user_change)
                    return jsonify(user[index])
    
        
#create user
@app.route('/users', methods=['POST'])
def create():
    new_user = request.get_json()
    user.append(new_user)
    return jsonify(user)

#delete user
@app.route('/user/<int:id>',methods=['DELETE'])
def delete(id):
    for index,user in enumerate(user):
        if user.get('id')  == id:
            del user[index]
    return jsonify(user)

#run the api
app.run(port=5000, host='localhost', debug=True)
