import pyrebase

config = {
    "apiKey": "AIzaSyDt8K9ooI85lqst9PC_axdAy01lPg16izM",
    "authDomain": "uw-strength-bot-user-info.firebaseapp.com",
    "databaseURL": "https://uw-strength-bot-user-info-default-rtdb.firebaseio.com",
    "projectId": "uw-strength-bot-user-info",
    "storageBucket": "uw-strength-bot-user-info.appspot.com",
    "messagingSenderId": "370976208515",
    "appId": "1:370976208515:web:82e41fe59656d482b70db6",
    "measurementId": "G-7MY9HL5Q5J"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
