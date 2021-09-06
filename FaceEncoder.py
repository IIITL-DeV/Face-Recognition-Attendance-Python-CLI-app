import face_recognition as fr
class FaceEncoder:

    def getImg(rollNo):
        
        try:
            img = fr.load_image_file(saveDir+"/"+rollNo+".jpeg")

        except  e:
            img = fr.load_image_file(FirebaseBucket().downloadFaceImg(rollNo))

        return img

    def getEcoding(self,rollNo,saveDir):
        img = None




        # img = read_img(known_dir + '/' + file)
        img_enc = face_recognition.face_encodings(img)[0]


        f = open('encodings.json',)
        
        # returns JSON object as 
        # a dictionary
        encodings = json.load(f)

        encodings[rollNo] = img_enc

        






    

