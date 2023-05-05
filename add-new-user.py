from flask import request, jsonify

@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    user_id = user_data['user_id']
    username = user_data['username']
    email = user_data['email']

    users_table = dynamodb.Table('Users')
    users_table.put_item(
        Item={
            'user_id': user_id,
            'username': username,
            'email': email
        }
    )

    return jsonify({'status': 'success', 'message': 'User registered'})
