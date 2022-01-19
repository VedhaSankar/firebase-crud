import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# /home/vedha/code/fries/creds

def connect_db():

    cred = credentials.Certificate("/home/vedha/code/fries/creds/fir-test.json")

    # Use the application default credentials
    firebase_admin.initialize_app(cred, {
    'projectId': 'fir-test-5b610',
    })

    db = firestore.client()

    return db

def insert_one():

    db = connect_db()

    doc_ref = db.collection('firebase-test').document('firebase-test')
    doc_ref.set({
        'first': 'Ada',
        'last': 'Lovelace',
        'born': 1815
    })

def read_data():

    db = connect_db()

    users_ref = db.collection(u'firebase-test')
    docs = users_ref.stream()

    for doc in docs:
        print(doc) # returns object
        print(doc.to_dict())

def start():

    read_data()


if __name__=='__main__':

    start()