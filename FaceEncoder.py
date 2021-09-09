import face_recognition as fr
import FirebaseBucket
import json

class FaceEncoder:
    saveDir="KnownFaces/"
    localJsonDir="CurrentFaceData.json/"
    encDir="encodings.json"

    def getEcoding(self,rollNo):
        FirebaseBucket.downloadFaceImg(rollNo)
        img=fr.load_image_file(self.saveDir+rollNo+".jpg")
        enc = fr.face_encodings(img)[0]
        FirebaseBucket.deleteImage(self,rollNo)
        return enc.tolist()
    
    def encodingUpdater(self):
        f=open(self.localJsonDir)
        f2=open(self.encDir)
        locData=json.load(f)
        fbData=FirebaseBucket.getChangedData()
        encData=json.load(f2)
        f.close()
        f2.close()
        
        for roll,dat in fbData.items():
            if (roll in locData and int(dat)>int(locData[roll])) or (roll not in locData):
                enc=self.getEcoding(roll)
                locData[roll]=int(dat)
                encData[roll]=enc
        
        f=open(self.localJsonDir,'w')
        f2=open(self.encDir,'w')
        json.dump(locData,f)
        json.dump(encData,f2)
        f.close()
        f2.close()