from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({'result': result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = data['a'] - data['b']
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = data['a'] * data['b']
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    result = data['a'] / data['b']
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)
