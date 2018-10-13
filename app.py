from flask import Flask, jsonify
from flask import request

app = Flask(__name__)



@app.route('/restapi', methods=['POST'])
def hello():
	user_str = request.json.get("userstr")
	if user_str == "Hello":
		myresponse="Hi!"
		return jsonify( myresponse )
	else:
		abort(404)#, {'message': 'Wrong input, Say "Hello"'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')