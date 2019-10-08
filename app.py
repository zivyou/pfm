from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    re = os.system('uname -a')
    return re.__str__

if __name__ == "__main__":
    app.run(debug=True, port=8080)
