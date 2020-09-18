from flask import Flask, render_template, url_for, request,redirect, flash
from categorie import categorie, sub_categorie
from forms import New_Item

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b148fa19990c223482e18e1e639f25af'

@app.route("/")
@app.route("/home/index")
def index():
    return render_template('home/index.html')

@app.route("/home/about")
def about():
    return render_template("/home/about.html")

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


@app.route("/home/pant")
def pant():
    return render_template("/home/pant.html")


@app.route("/home/shoe")
def shoe():
    return render_template("/home/shoe.html")

@app.route("/home/other")
def other():
    return render_template("/home/other.html")



@app.route("/upload_items/upload_item", methods=['GET', 'POST'])
def new_item():
    form = New_Item()
    if form.validate_on_submit():
        print(form.product_name)
        print(form.product_price)
        print(form.description)
        return redirect(url_for('index'))
    return render_template("/upload_items/upload_item.html", 
                           categorie = categorie, sub_categorie = sub_categorie, form = form)

if __name__ == "__main__":
    app.run(debug= True)