#FOR TESTING FEATURE AND ADDING STUFF ONLY
'''import json
import face_recognition as fr

img=fr.load_image_file("KnownFaces/lit2019066.jpg")
enc = fr.face_encodings(img)[0]

x={
    "lit2019066":enc.tolist()
}
y=json.dumps(x)
f=open("encodings.json","a")
f.write(y)
f.close()'''