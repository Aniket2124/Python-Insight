from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '{"name": "ani", "age": 29, "city": "York", "actor": "aaa"}'


@app.route('/getJson')
def hello_world2():
    return '{"name": "abi", "age": 29, "city": "York", "actor": "aaa"}'


@app.route('/connect_to_the_game')
def hello_world3():
    return '{"name": "abi", "age": 29, "city": "York", "actor": "aaa"}'


if __name__ == '__main__':
    # app.run(host='192.168.0.104', port=4000)
    app.run(debug=True)
