import face_recognition as fr
from FirebaseBucket import FirebaseBucket
import json
from pathlib import Path

class FaceEncoder:
    src=str(Path().resolve())
    saveDir="KnownFaces/"
    localJsonDir=src+"/ChangedData.json"
    encDir=src+"/encodings.json"
    fbb=FirebaseBucket()

    def getEncoding(self,rollNo):
        self.fbb.downloadFaceImg(rollNo)
        img=fr.load_image_file(self.saveDir+rollNo+".jpg")
        enc = fr.face_encodings(img)[0]
        # self.fbb.deleteImage(rollNo)
        return enc.tolist()
    
    def create_new_class(self, class_info):
        self.fbb.createClass(class_info)
    
    def update_class_total(self,name):
        self.fbb.updateCLassTotal(name)

    def update_presence_of_student(self,roll,class_name):
        self.fbb.updatePresence(roll,class_name)

    def encodingUpdater(self):
        print("Updating student info, please wait.")
        self.fbb.updateStudentInfo()
        print("Running Encoding updater, please wait.")
        f=open(self.localJsonDir)
        f2=open(self.encDir)

        locData=json.load(f)
        fbData=self.fbb.getChangedData()
        encData=json.load(f2)
        f.close()
        f2.close()

        for roll,dat in fbData.items():
            if (roll in locData and int(dat)>int(locData[roll])) or (roll not in locData):
                enc=self.getEncoding(roll)
                locData[roll]=int(dat)
                encData[roll]=enc
                # print(encData)
        
        f=open(self.localJsonDir,'w')
        f2=open(self.encDir,'w')
        json.dump(locData,f)
        json.dump(encData,f2)
        f.close()
        f2.close()
        class_info=self.fbb.getCurrentClass()
        return class_info