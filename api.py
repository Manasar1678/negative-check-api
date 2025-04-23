from flask import Flask, jsonify, request

app = Flask(__name__)
shared_data = {"number": 0}

@app.route('/set_number', methods=['POST'])
def set_number():
    data = request.get_json()
    shared_data['number'] = data.get('number', 0)
    return jsonify({"message": "Number saved"})

@app.route('/is_negative', methods=['GET'])
def is_negative():
    return jsonify({'is_negative': shared_data['number'] < 0})

if __name__ == '__main__':
    app.run(port=5000)

