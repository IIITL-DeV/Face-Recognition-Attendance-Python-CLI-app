import face_recognition as fr
import FirebaseBucket
import json

class FaceEncoder:

    def getImg(rollNo,saveDir):
        try:
            img = fr.load_image_file(saveDir+"/"+rollNo+".jpeg")
        except:
            img = fr.load_image_file(FirebaseBucket().downloadFaceImg(rollNo))
        return img

    def getEcoding(self,rollNo,saveDir):
        img = None
        # img = read_img(known_dir + '/' + file)
        img_enc = fr.face_encodings(img)[0]
        f = open('encodings.json',)
        # returns JSON object as 
        # a dictionary
        encodings = json.load(f)

        encodings[rollNo] = img_enc

        






    

