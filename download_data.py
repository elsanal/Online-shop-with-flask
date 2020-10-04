def getShoe():
    data = firestore.collection(u'shoe').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs    

def getWatch():
    data = firestore.collection(u'shoe').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

def getPhone():
    data = firestore.collection(u'shoe').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

def getClothe():
    data = firestore.collection(u'shoe').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

def getPant():
    data = firestore.collection(u'shoe').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

def getOther():
    data = firestore.collection(u'shoe').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 

def getBag():
    data = firestore.collection(u'shoe').get()
    docs = []
    for doc in data:
        docs.append(doc.to_dict())
    return docs 
