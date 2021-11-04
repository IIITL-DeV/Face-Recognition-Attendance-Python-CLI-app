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
        configpath=str(Path().resolve())+'/firebaseconfig.json'
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)
        
        con=open(configpath)
        firebaseConfig=json.load(con)
        firebaseConfig["serviceAccount"]=path

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
            return 0
    
    def createClass(self, clsinfo):
        ref=self.db.collection('classes').document(clsinfo['subject']+clsinfo['batchyear'])
        ref.set(clsinfo)

    def updateCLassTotal(self, name):
        ref=self.db.collection('classes').document(name)
        doc=ref.get()
        if doc.exists:
            doc=doc.to_dict()
            temp=int(doc['total'])+1
            ref.update({'total':str(temp)})
        else:
            print("Class not found")
    
    #sum total of all classes of a particular subject
    def getTotalClasses(self,subject):
        ref=self.db.collection('classes').document(subject)
        doc=ref.get()
        if doc.exists:
            doc=doc.to_dict()
            return doc["total"]
        else:
            print("Class not found")

    def updatePresence(self,roll,class_name):
        cls=class_name
        class_name=class_name[0:len(class_name)-4]
        ref=self.db.collection(roll).document(class_name)
        doc=ref.get()
        x=int(self.getTotalClasses(cls))
        if doc.exists:
            doc=doc.to_dict()
            temp=int(doc['total'])+1
            temp2=str(round(((int(temp))/x)*100,2))
            ref.update({'total':str(temp)})
            ref.update({'percentage':str(temp2)})
        else:
            temp=dict()
            temp["percentage"]=str(round((1/x)*100,2))
            temp["total"]='1'
            temp["subject"]=class_name
            ref.set(temp)



    def updateStudentInfo(self):
        ref=self.db.collection("students")
        students=ref.stream()
        info=dict()
        for s in students:
            info[s.id]=s.to_dict()
        f = open('StudentInfo.json','w')
        json.dump(info,f)