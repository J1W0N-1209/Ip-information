from flask import Flask,render_template,request
import os ,requests

app = Flask(__name__)

@app.route('/',methods = ["GET","POST"])
def index():
  if request.method == "POST":
    ip = request.form["ip"]
    response= requests.get(f"http://ip-api.com/json/{ip}")
  return render_template('index.html',response=response.json())

if __name__ == '__main__':
  app.run(debug=True)