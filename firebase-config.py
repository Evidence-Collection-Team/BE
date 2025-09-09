import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("./config/gbswoutsode-firebase-adminsdk-fbsvc-877e69251d.json")
firebase_admin.initialize_app(cred)
