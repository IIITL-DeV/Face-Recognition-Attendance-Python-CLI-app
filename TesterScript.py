from FirebaseBucket import FirebaseBucket

fb=FirebaseBucket()
fb.getCurrentClass()


# import WorkbookWriter as waw
# from datetime import date
# src='/home/gustav/Documents/Code/Project/FaceRecognitionAttendance/AttendanceSheets/'
# name='VKS'+str(date.today())[:7]
# w=waw.WorkbookWriter(name)
# w.write('LIT2019001','Mohsin',True)
# subject=''
# name=subject+str(date.today())[:7]
# wb = Workbook()
# ws = wb.create_sheet(title='SoftwareEngineering', index=0)

# ws['A1']='Roll Number'
# ws['B1']='Name'
# ws['']
# wb.save(s) 
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