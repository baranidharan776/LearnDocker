from flask import Flask
import os
app = Flask(__name__)
@app.route('/')

def hello()
    return ('\n Hello from container world !!!! \n\n')
if name == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)
