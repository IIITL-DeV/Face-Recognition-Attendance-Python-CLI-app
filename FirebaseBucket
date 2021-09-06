import firebase_admin
from firebase_admin import credentials

import pyrebase
import json


class FirebaseBucket:
    def __init__(self):
        # cred = credentials.Certificate("/content/pythonfirebasebucket.json")
# firebase_admin.initialize_app(cred)

        firebaseConfig = {
            "apiKey": "AIzaSyDgBG1Nhd69HTitzbXW4vPz9SBlYsAKIdw",
            "authDomain": "pythonfirebasebucket.firebaseapp.com",
            "projectId": "pythonfirebasebucket",
            "databaseURL":"https://pythonfirebasebucket.firebaseio.com",
            "storageBucket": "pythonfirebasebucket.appspot.com",
            "messagingSenderId": "767588793860",
            "appId": "1:767588793860:web:08dfb9a3d51fdd6cee3f51",
            "measurementId": "G-1EMCQRDRW6",
            "serviceAccount":"/content/pythonfirebasebucket.json"
        }


        firebaseStorage = pyrebase.initialize_app(firebaseConfig)

        self.storage = firebaseStorage.storage()
        self.newFaces = []
        self.delFaces = []

        

    def upload(self,localFilePath,firebaseFilePath):
        
        self.storage.child(firebaseFilePath).put(localFilePath)

    
    def downloadFaceImg(self,rollNo:str,saveDir):
        
        
        self.storage.child("faces/"+rollNo+".jpeg").download(saveDir+"/"+rollNo+".jpeg")
    
        return saveDir+"/"+rollNo+".jpeg"
    
    def getChangedData(self):
        
        self.storage.child("ChangedData.json").download("ChangedData.json")

        # Opening JSON file
        f = open('ChangedData.json',)
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)

        self.newFaces = data["newFaces"]
        self.delFaces = data["delFaces"]

        return self.newFaces,self.delFaces

