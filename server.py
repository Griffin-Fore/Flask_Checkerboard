from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Baseboard():
    return render_template("index.html")

@app.route('/4')
def Base4():
    return render_template("index.html",y=4)

@app.route('/<int:x>/<int:y>')
def BaseXbyY(x,y):
    return render_template("index.html",x=x,y=y)

@app.route('/<int:x>/<int:y>/<string:colora>/<string:colorb>')
def BaseColor(x,y,colora,colorb):
    return render_template("index.html",x=x,y=y,colora=colora,colorb=colorb)

if __name__=="__main__":
    app.run(debug=True)