import firebase_admin
from firebase_admin import credentials
from firebase_admin import db,storage,auth,firestore

# Fetch the service account key JSON file contents
cred = credentials.Certificate('codigo6-92662-firebase-adminsdk-bljqh-497714c89a.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    
    "databaseURL": "https://codigo6-92662-default-rtdb.firebaseio.com",    
    "storageBucket": "codigo6-92662.appspot.com"
})

ds = storage.bucket()






# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import storage

# cred = credentials.Certificate('codigo6-92662-firebase-adminsdk-bljqh-497714c89a.json')
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'gs://codigo6-92662.appspot.com'
# })

# bucket = storage.bucket()