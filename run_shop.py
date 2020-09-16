from flask import Flask, render_template, url_for, request,redirect, flash



app = Flask(__name__)


@app.route("/")
@app.route("/home/index")
def index():
    return render_template('home/index.html')

@app.route("/home/about")
def about():
    return render_template("/home/about.html")

@app.route("/home/computer")
def computer():
    return render_template("/home/computer.html")

@app.route("/home/phone")
def phone():
    return render_template("/home/phone.html")

@app.route("/home/watch")
def watch():
    return render_template("/home/watch.html")

@app.route("/home/clothe")
def clothe():
    return render_template("/home/clothe.html")

@app.route("/home/bag")
def bag():
    return render_template("/home/bag.html")

@app.route("/home/electronic")
def electronic():
    return render_template("/home/electronic.html")

@app.route("/home/construction")
def construction():
    return render_template("/home/construction.html")

@app.route("/home/agro_bussiness")
def agro_bussiness():
    return render_template("/home/agro_bussiness.html")

@app.route("/home/shoe")
def shoe():
    return render_template("/home/shoe.html")

@app.route("/home/other")
def other():
    return render_template("/home/other.html")

if __name__ == "__main__":
    app.run(debug= True)