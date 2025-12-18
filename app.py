from flask import Flask,render_template
import similarity_check as sc
import os


app = Flask(__name__)

@app.route('/')
def home():
    check = sc.similarity_check("food","Food")
    return render_template('home.html', check = check)

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port = port)