import numpy as np
import face_recognition as fr
import cv2
import json
from FaceEncoder import FaceEncoder
from WorkbookWriter import WorkbookWriter as wbw

fe=FaceEncoder()
class_info=fe.encodingUpdater()
flags=dict()
if class_info==0:
    print("No classes scheduled right now, do you still want to continue? (Y/N)")
    if input().lower=='y':
        print("Starting a new class")
        class_info=dict()
        class_info["subject"]=input("Enter subject, example Cryptography\n")
        class_info["batch"]=input("Enter batch example IT, CS etc \n")
        class_info["batchyear"]=input("Enter batch year, example 2019 \n")
        class_info['total']='0'
        fe.create_new_class(class_info)
    else:
        print("Shutting down program \n")
        quit()
fe.update_class_total(class_info['subject']+class_info['batchyear'])
print("Updating finished, now running webcam")


class_name=class_info["subject"]+class_info["batchyear"]
wb=wbw(class_name)

video_capture = cv2.VideoCapture(0)

known_face_encondings = list()
known_face_names = list()
f=open("encodings.json")
f2=open("StudentInfo.json")

studentinfo=json.load(f2)
all_face_encodings=json.load(f)
f.close()
for roll,enc in all_face_encodings.items():
    known_face_names.append(roll)
    known_face_encondings.append(np.array(enc))

while True: 
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = fr.compare_faces(known_face_encondings, face_encoding)

        name = "Unknown"

        face_distances = fr.face_distance(known_face_encondings, face_encoding)

        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            if name not in flags:
                wb.write(name,studentinfo[name]['name'],True)
                fe.update_presence_of_student(name,class_name)
                flags[name]=1

        #code below makes the rectangle so can be removed when needed
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Webcam_facerecognition', frame)
    #this if block closes the window if you press q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Webcam closed due to intervention by user")
        break

video_capture.release()
cv2.destroyAllWindows()