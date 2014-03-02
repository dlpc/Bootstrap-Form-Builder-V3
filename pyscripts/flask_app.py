from flask import Flask, jsonify, url_for
import os

static_folder=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, 
             static_folder=static_folder)

@app.route("/index")
def index_view():
    
    return "<a href=%s>index<a/>" % url_for('static', filename='index.html')

if __name__ == "__main__":
    app.run(
        port=5000,
        debug=True
            )