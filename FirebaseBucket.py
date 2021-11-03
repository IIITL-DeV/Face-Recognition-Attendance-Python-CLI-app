import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pathlib import Path
import pyrebase
import json
from datetime import datetime


class FirebaseBucket:

    def __init__(self):
        path=str(Path().resolve())+"/pythonfirebasebucket.json"
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)

        firebaseConfig = {
            "apiKey": "AIzaSyDgBG1Nhd69HTitzbXW4vPz9SBlYsAKIdw",
            "authDomain": "pythonfirebasebucket.firebaseapp.com",
            "projectId": "pythonfirebasebucket",
            "databaseURL":"https://pythonfirebasebucket.firebaseio.com",
            "storageBucket": "pythonfirebasebucket.appspot.com",
            "messagingSenderId": "767588793860",
            "appId": "1:767588793860:web:08dfb9a3d51fdd6cee3f51",
            "measurementId": "G-1EMCQRDRW6",
            "serviceAccount":path
        }


        firebaseStorage = pyrebase.initialize_app(firebaseConfig)
        self.saveDir="FaceRecognitionAttendance/KnownFaces/"
        self.storage = firebaseStorage.storage()
        self.newFaces = []
        self.delFaces = []
        self.db = firestore.client()

        
    def deleteImage(self,rollNo):
        blob = self.storage.blob("faces/"+rollNo+".jpeg")
        print("Deleting",blob)
        blob.delete()

    def upload(self,localFilePath,firebaseFilePath):
        
        self.storage.child(firebaseFilePath).put(localFilePath)

    
    def downloadFaceImg(self,rollNo):
        
        
        self.storage.child("faces/"+rollNo+".jpeg").download(self.saveDir+"/"+rollNo+".jpeg")
    
        return self.saveDir+"/"+rollNo+".jpeg"
    
    def getChangedData(self):
        
        self.storage.child("ChangedData.json").download("ChangedData.json")

        # Opening JSON file
        f = open('ChangedData.json',)
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        return data

    def getCurrentClass(self):
        ref=self.db.collection("classes")
        classes=ref.stream()
        t=datetime.now()
        hook=str(t.hour)+str(t.minute)
        for c in classes:
            name=c.id
            info=c.to_dict()
            if int(info['starttime'])<=int(hook) and int(info['endtime'])>int(hook):
                print("Current class is: "+name)
                info["name"]=name
                return info