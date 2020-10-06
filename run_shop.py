from flask import Flask, render_template, url_for, request,redirect, flash
from categorie import categorie, sub_categorie
from forms import (New_Item, Login, Register, AddBag, AddPhone,
                   AddClothe, AddOther, AddPant, AddShoe, AddWatch)
import firebase_admin
from firebase import storage, Firebase 
from firebase_admin import credentials
from firebase_admin import firestore, storage
import os, secrets
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b148fa19990c223482e18e1e639f25af'

cred = credentials.Certificate("firebase-sdk.json")
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
    docBag = getBag()
    docShoe = getShoe()
    docClothe = getClothe()
    docOther = getOther()
    docPant = getPant()
    docPhone = getPhone()
    docWatch = getWatch()   
    return render_template('home/index.html', docOther = docOther, docPant = docPant,docPhone = docPhone
                           ,docBag = docBag, docShoe = docShoe, docClothe = docClothe, docWatch = docWatch)

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
        if form.picture.data:
            picture = save_pic(form.picture.data)
            picture_path = os.path.join(app.root_path,'photos',picture)
            saveProduct_toDatabase(form, picture, picture_path,form.product_type)
            os.remove(picture_path)
            return redirect(url_for('bag',admin = 'admin'))
    return render_template("/admin/addBag.html", form = form)

@app.route("/admin/addClothe",methods=['GET', 'POST'])
def addClothe():
    form = AddClothe()
    if form.validate_on_submit():
        if form.picture.data:
            picture = save_pic(form.picture.data)
            picture_path = os.path.join(app.root_path,'photos',picture)
            saveProduct_toDatabase(form, picture, picture_path,form.product_type)
            os.remove(picture_path)
            return redirect(url_for('clothe', admin = 'admin'))
    return render_template("/admin/addClothe.html", form = form)

@app.route("/admin/addOther",methods=['GET', 'POST'])
def addOther():
    form = AddOther()
    if form.validate_on_submit():
        if form.picture.data:
            picture = save_pic(form.picture.data)
            picture_path = os.path.join(app.root_path,'photos',picture)
            saveProduct_toDatabase(form, picture, picture_path,form.product_type)
            os.remove(picture_path)
            return redirect(url_for('other', admin = 'admin'))
    return render_template("/admin/addOther.html", form = form)

@app.route("/admin/addPant",methods=['GET', 'POST'])
def addPant():
    form = AddPant()
    if form.validate_on_submit():
        if form.picture.data:
            picture = save_pic(form.picture.data)
            picture_path = os.path.join(app.root_path,'photos',picture)
            saveProduct_toDatabase(form, picture, picture_path,form.product_type)
            os.remove(picture_path)
            return redirect(url_for('pant', admin = 'admin'))
    return render_template("/admin/addPant.html", form = form)

@app.route("/admin/addShoe",methods=['GET', 'POST'])
def addShoe():
    form = AddShoe()
    if form.validate_on_submit():
        if form.picture.data:
            picture = save_pic(form.picture.data)
            picture_path = os.path.join(app.root_path,'photos',picture)
            saveProduct_toDatabase(form, picture, picture_path,form.product_type)
            os.remove(picture_path)
            return redirect(url_for('shoe', admin = 'admin'))
    return render_template("/admin/addShoe.html", form = form)

@app.route("/admin/addWatch",methods=['GET', 'POST'])
def addWatch():
    form = AddWatch()
    if form.validate_on_submit():
        if form.picture.data:
            picture = save_pic(form.picture.data)
            picture_path = os.path.join(app.root_path,'photos',picture)
            saveProduct_toDatabase(form, picture, picture_path,form.product_type)
            os.remove(picture_path)
            return redirect(url_for('watch', admin = 'admin'))
    return render_template("/admin/addWatch.html", form = form)

@app.route("/admin/addPhone",methods=['GET', 'POST'])
def addPhone():
    form = AddPhone()
    if form.validate_on_submit():
        if form.picture.data:
            picture = save_pic(form.picture.data)
            picture_path = os.path.join(app.root_path,'photos',picture)
            saveProduct_toDatabase(form, picture, picture_path,form.product_type)
            os.remove(picture_path)
            return redirect(url_for('phone', admin = 'admin'))
    return render_template("/admin/addPhone.html", form = form)

# ##############################################################################

#################################################################################
@app.route("/home/phone")
@app.route("/home/phone/<string:admin>")
def phone(admin):
    docs = getPhone()
    return render_template("/home/phone.html", admin = admin, docs = docs)

@app.route("/home/watch")
@app.route("/home/watch/<string:admin>")
def watch(admin):
    docs = getWatch()
    return render_template("/home/watch.html", admin = admin, docs = docs)


@app.route("/home/clothe")
@app.route("/home/clothe/<string:admin>")
def clothe(admin):
    docs = getClothe()
    return render_template("/home/clothe.html", admin = admin, docs = docs)

@app.route("/home/bag")
@app.route("/home/bag/<string:admin>")
def bag(admin):
    docs = getBag()
    return render_template("/home/bag.html", admin = admin, docs = docs)


@app.route("/home/pant")
@app.route("/home/pant/<string:admin>")
def pant(admin):
    docs = getPant()
    return render_template("/home/pant.html", admin = admin, docs = docs)


@app.route("/home/shoe")
@app.route("/home/shoe/<string:admin>")
def shoe(admin):
    docs = getShoe()
    return render_template("/home/shoe.html", admin = admin, docs = docs)

@app.route("/home/other")
@app.route("/home/other/<string:admin>")
def other(admin):
    docs = getOther()
    return render_template("/home/other.html", admin = admin, docs = docs)

@app.route("/details/detail")
@app.route("/details/detail/<int:index>/<string:categ>")
def detail(index,categ):
    docs = []
    if categ == 'bag':
        docs = getBag()  
    elif categ == 'shoe':
        docs = getShoe()
    elif categ == 'clothe':
        docs = getClothe()
    elif categ == 'phone':
        docs = getPhone()
    elif categ == 'other':
        docs = getOther()
    elif categ == 'pant':
        docs = getPant()
    else :
        docs = getWatch()          
    return render_template("/details/detail.html", docs = docs, index = index)

#############################################################################

############################################################################

@app.route("/auth/register",methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        if u'{}'.format(request.form.get('password'))=='123456' and u'{}'.format(request.form.get('email'))=='sana@gmail.com':
            print(form.email)
            print(form.password)
            return redirect(url_for('login'))
    return render_template("/auth/register.html", form = form)

@app.route("/auth/login",methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        doc = getAdmin()
        password = doc[0]['password']
        email1 = doc[0]['email1']
        email2 = doc[0]['email2']
        formPassword = u'{}'.format(request.form.get('password'))
        formEmail = u'{}'.format(request.form.get('email'))
        if (formEmail==email1 or formEmail == email2) and formPassword==password:
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

def save_pic(form_pic):
    random_hex = secrets.token_hex(8)
    _,file_ext = os.path.splitext(form_pic.filename)
    picture_name = random_hex + file_ext
    picture_path = os.path.join(app.root_path,'photos',picture_name)
    form_pic.save(picture_path)
    out_size = (300,300)
    image = Image.open(form_pic)
    image.thumbnail(out_size)
    image.save(picture_path)
    return picture_name

def saveProduct_toDatabase(form, picture, picture_path, product_type):
    firebase.storage().child(product_type).child(picture).put(picture_path)
    pictureUrl = firebase.storage().child(product_type).child(picture).get_url(None)
    docRef = firestore.collection(product_type)
    docRef.add({
    u'product_name' : u'{}'.format(request.form.get('product_name')),
    u'description' : u'{}'.format(request.form.get('description')),
    u'product_price' : u'{}'.format(request.form.get('product_price')),
    u'type' : u'{}'.format(form.product_type),
    u'picture' : pictureUrl,
    u'order': u'{}'.format(form.order),
    })  
    
################################################################################

#################################################################################

def getShoe():
    data = firestore.collection(u'shoe').order_by(u'order',direction= 'DESCENDING').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs    

def getWatch():
    data = firestore.collection(u'watch').order_by(u'order',direction= 'DESCENDING').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

def getPhone():
    data = firestore.collection(u'phone').order_by(u'order',direction= 'DESCENDING').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

def getClothe():
    data = firestore.collection(u'clothe').order_by(u'order',direction= 'DESCENDING').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

def getPant():
    data = firestore.collection(u'pant').order_by(u'order',direction= 'DESCENDING').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

def getOther():
    data = firestore.collection(u'other').order_by(u'order',direction= 'DESCENDING').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

def getBag():
    data = firestore.collection(u'bag').order_by(u'order',direction= 'DESCENDING').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 
def getAdmin():
    data = firestore.collection(u'admin').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

if __name__ == "__main__":
    app.run(debug= True)