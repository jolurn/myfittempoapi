
import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyAJ-sLrTTI9a-MVaPm9UWgqka8Ol27DNE4",
    "authDomain": "codigogym-cd01b.firebaseapp.com",
    # "databaseURL": "https://codigogym-cd01b.appspot.com",
    "databaseURL": "gs://codigogym-cd01b.appspot.com",
    "projectId": "codigogym-cd01b",
    "storageBucket": "codigogym-cd01b.appspot.com",
    "messagingSenderId": "544516201306",
    "appId": "1:544516201306:web:7eaaeb19cd39d0e5553163",
    "serviceAccount": "../../serviceAccountKey.json"
  }

firebase_storage = pyrebase.initialize_app(firebaseConfig)
storage = firebase_storage.storage()

storage.child("img/a.jpg").put("../img/img/a.jpg")