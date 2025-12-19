from flask import Flask,render_template,request,url_for
import similarity_check as sc
import os


app = Flask(__name__)



@app.route('/' , methods = ["GET","POST"])
def text():

    score = None

    if request.method == "POST":
        text1 = request.form.get('text1')
        text2 = request.form.get('text2')

        score = sc.similarity_check(text1,text2)
    return render_template('text.html', score = score)


if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port = port)