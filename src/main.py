from Clases.QLDBDriver import QLDBDriver
from pyqldbsamples.model.sample_data import print_result
from flask import Flask, request
from Clases.Service import Service

app = Flask(__name__)
service = Service()

def response(modulo, mensaje, datos, error, request):
    resp = {
        "error": error,
        "datos": datos,
        "mensaje": mensaje,
        "modulo": modulo
    }

    service.save_ws_log(request, resp)

    return resp

@app.route('/validateUser', methods=['POST'])
def validate_user():
    data = request.get_json()
    user = data.get('user', "")
    password = data.get('pass', "")

    if user == "" or password == "":
        return response('validateUser', 'No password or user', "False", "1", data)

    rst = service.validate_user(user, password)

    if not rst:
        return response('validateUser', 'Invalid password', "False", "1", data)

    return response('validateUser', 'User validated', "True", "0", data)


@app.route('/createUser', methods=['POST'])
def create_user():
    data = request.get_json()
    user = data.get('user', "")
    password = data.get('pass', "")

    if user == "" or password == "":
        return response('createUser', 'No password or user', "False", "1", data)

    service.create_user(user, password)

    return response('createUser', 'Created user successfully', "True", "0", data)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
