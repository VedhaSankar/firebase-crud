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

def write_data(db):

    doc_ref = db.collection('firebase-test').document('firebase-test')
    doc_ref.set(
    {
        'first' : 'Ada',
        'last'  : 'Lovelace',
        'born'  : 1812
    }
    )

def read_data(db):

    users_ref = db.collection(u'firebase-test')
    docs = users_ref.stream()

    for doc in docs:
        print(doc) # returns object
        print(doc.to_dict())

def delete_data(db):


    db.collection('firebase-test').document('firebase-test').delete()

def start():

    db = connect_db()

    # write_data(db)
    read_data(db)
    # delete_data(db)


if __name__=='__main__':

    start()