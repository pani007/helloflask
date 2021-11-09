from flask import Flask
app = Flask(__name__)

@app.route("/",methods=["GET"])
def hello():
    return "<h1> Hello World</h1>"

app.run()