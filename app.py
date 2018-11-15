from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route("/", methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

if __name__ == '__main__':
    app.run(debug=True)