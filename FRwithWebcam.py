import numpy as np
import face_recognition as fr
import cv2
import json
import FaceEncoder

print("Running Encoding updater, please wait.")
#FaceEncoder.encodingUpdater()
print("Updating finished, now running webcam")

video_capture = cv2.VideoCapture(0)

known_face_encondings = list()
known_face_names = list()
f=open("encodings.json")
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