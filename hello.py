## question B.1 .i ###
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    """This function does blah blah."""
    return "Hello world !"
## question B.1.ii ###
@app.route('/hello/linda')
def optional():
    """This function returns Hello <name>"""
    return "Hello "

if __name__ == "__main__":
    app.run()
