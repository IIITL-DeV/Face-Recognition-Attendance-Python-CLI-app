#FOR TESTING FEATURE AND ADDING STUFF ONLY
'''
import json
import face_recognition as fr

img=fr.load_image_file("FaceRecognitionAttendance/KnownFaces/lit2019066.jpg")
enc = fr.face_encodings(img)[0]

x={
    "lit2019066":enc.tolist()
}
helloo
f=open("FaceRecognitionAttendance/encodings.json","w")
y=json.dump(x,f)
f.close()'''