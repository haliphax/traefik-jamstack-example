from flask import Flask
from json import dumps

app = Flask(__name__)

@app.route("/api")
def api():
    return dumps({
        "content": "I am not! Fooled you!"
    })


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)

