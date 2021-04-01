## question B.1 .i ###
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world !"
## question B.1.ii ###
@app.route('/hello/linda')
def optional():
    return "Hello "
if __name__ == "__main__":
    app.run()