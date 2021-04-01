from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
return "Hello world !"
@app.route('/hello/linda')
def optional():
return "Hello "
if __name__ == "__main__":
 app.run()