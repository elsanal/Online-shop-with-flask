from flask import Flask, render_template, url_for, request,redirect, flash
from categorie import categorie, sub_categorie
from forms import (New_Item, Login, Register, AddBag, AddPhone,
                   AddClothe, AddOther, AddPant, AddSheo, AddWatch)
import firebase_admin
from firebase import storage, Firebase 
from firebase_admin import credentials
from firebase_admin import firestore, storage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b148fa19990c223482e18e1e639f25af'

cred = credentials.Certificate("/Users/sanaaloute/important_files/firebase-sdk.json")
firebase_admin.initialize_app(cred)
firestore = firestore.client()

firebaseConfig = {
            'apiKey': "AIzaSyA2iVYIp_WtG4Mh1Kpy98cX1rG4SXruzoY",
            'authDomain': "alishop-259be.firebaseapp.com",
            'databaseURL': "https://alishop-259be.firebaseio.com",
            'projectId': "alishop-259be",
            'storageBucket': "alishop-259be.appspot.com",
            'messagingSenderId': "12974745289",
            'appId': "1:12974745289:web:6fb753a559fc3c7e02cf18",
            'measurementId': "G-T4VBJRR6P8"
        }

firebase = Firebase(firebaseConfig)
database = firebase.database()
isAdmin = False

@app.route("/")
@app.route("/home/index")
def index():   
    return render_template('home/index.html')

@app.route("/home/about")
def about():
    return render_template("/home/about.html")
#####################################################################################

######################################################################################
@app.route("/admin/admin")
def admin():
    return render_template("/admin/admin.html")

@app.route("/admin/addBag",methods=['GET', 'POST'])
def addBag():
    form = AddBag()
    if form.validate_on_submit():
        return redirect(url_for('bag',admin = 'admin'))
    return render_template("/admin/addBag.html", form = form)

@app.route("/admin/addClothe",methods=['GET', 'POST'])
def addClothe():
    form = AddClothe()
    if form.validate_on_submit():
        return redirect(url_for('clothe', admin = admin))
    return render_template("/admin/addClothe.html", form = form)

@app.route("/admin/addOther",methods=['GET', 'POST'])
def addOther():
    form = AddOther()
    if form.validate_on_submit():
        return redirect(url_for('other', admin = admin))
    return render_template("/admin/addOther.html", form = form)

@app.route("/admin/addPant",methods=['GET', 'POST'])
def addPant():
    form = AddPant()
    if form.validate_on_submit():
        return redirect(url_for('pant', admin = admin))
    return render_template("/admin/addPant.html", form = form)

@app.route("/admin/addSheo",methods=['GET', 'POST'])
def addSheo():
    form = AddSheo()
    if form.validate_on_submit():
        return redirect(url_for('sheo', admin = admin))
    return render_template("/admin/addSheo.html", form = form)

@app.route("/admin/addWatch",methods=['GET', 'POST'])
def addWatch():
    form = AddWatch()
    if form.validate_on_submit():
        return redirect(url_for('watch', admin = admin))
    return render_template("/admin/addWatch.html", form = form)

@app.route("/admin/addPhone",methods=['GET', 'POST'])
def addPhone():
    form = AddPhone()
    if form.validate_on_submit():
        return redirect(url_for('phone', admin = admin))
    return render_template("/admin/addPhone.html", form = form)

# ##############################################################################

#################################################################################
@app.route("/home/phone")
@app.route("/home/phone/<string:admin>")
def phone(admin):
    return render_template("/home/phone.html", admin = admin)


@app.route("/home/watch")
@app.route("/home/watch/<string:admin>")
def watch(admin):
    return render_template("/home/watch.html", admin = admin)


@app.route("/home/clothe")
@app.route("/home/clothe/<string:admin>")
def clothe(admin):
    return render_template("/home/clothe.html", admin = admin)

@app.route("/home/bag")
@app.route("/home/bag/<string:admin>")
def bag(admin):
    return render_template("/home/bag.html", admin = admin)


@app.route("/home/pant")
@app.route("/home/pant/<string:admin>")
def pant(admin):
    admin = admin
    return render_template("/home/pant.html", admin = admin)


@app.route("/home/sheo")
@app.route("/home/sheo/<string:admin>")
def shoe(admin):
    return render_template("/home/shoe.html", admin = admin)

@app.route("/home/other")
@app.route("/home/other/<string:admin>")
def other(admin):
    return render_template("/home/other.html", admin = admin)

#############################################################################

@app.route("/auth/register",methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        print(form.email)
        print(form.password)
        return redirect(url_for('login'))
    return render_template("/auth/register.html", form = form)

@app.route("/auth/login",methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        return redirect(url_for('admin')) 
    return render_template("auth/login.html", form = form)

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