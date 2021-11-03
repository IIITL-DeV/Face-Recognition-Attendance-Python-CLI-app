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
        self.saveDir="KnownFaces/"
        self.storage = firebaseStorage.storage()
        self.newFaces = []
        self.delFaces = []
        self.db = firestore.client()

        
    # def deleteImage(self,rollNo):
    #     self.storage.child(("faces/"+rollNo)).remove
    #     print("Deleting",blob)
    #     blob.delete()

    def upload(self,localFilePath,firebaseFilePath):
        
        self.storage.child(firebaseFilePath).put(localFilePath)

    
    def downloadFaceImg(self,rollNo):
        self.storage.child("faces/"+rollNo).download(self.saveDir+rollNo+'.jpg')
        # except:
        #     print("Download Failed")
    
    def getChangedData(self):
        data=dict()
        ref=self.db.collection("students")
        students=ref.stream()
        for s in students:
            temp=s.to_dict()
            data[s.id]=temp["lastupdated"]
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
    
    def updateStudentInfo(self):
        ref=self.db.collection("students")
        students=ref.stream()
        info=dict()
        for s in students:
            info[s.id]=s.to_dict()
        f = open('StudentInfo.json','w')
        json.dump(info,f)