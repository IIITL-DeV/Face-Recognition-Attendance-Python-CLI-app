# Face-Recognition Attendance: Python CLI app
This repository contains the code for the Python CLI app. 

## By 
Group 3 

## Members
Hriday Grover - LIT2019042 

Mohsin Ahmed - LIT2019066 

Mark Andrew - LIT201940 

Bhanu Prakash Singh - LIT201943

Rajat Napalchyal - LIT2019076


## Overview
Our project aims to automate the conventional attendance management system for both ends (students and teachers) by using machine learning model 
of face recognition and a mobile application.

Additionally, the android application counterpart for students and teachers allows for teachers to access Realtime updating of classes and schedules. And using this database and the CNN algorithms done on the live surveillance updating the database, the students can retrieve information about their latest attendance percentage, records for each class they're enrolled in.

## How to run
##### Requirements: 
Python 3.5 or higher, pip
python modules: numpy, opencv, face_recognition, pyrebase, firebase_admin, openpyxl
(python modules are installed by opening command prompt and writing pip3 install <module_name>)

##### Firebase requirement:
This project uses Firebase for its cloud facilities. Since we have used our account for testing this project and it’s credentials can’t be shared for obvious privacy reasons, one has to sign up on Firebase and create a Project along with activating Firebase storage and Firestore. The credentials .json file should be saved in the project directory with the exact name  firebaseconfig.json. Another json file should be saved corresponding to the Firebase storage credentials with the exact name pythonfirebasebucket.json. These files contain private keys and should not be shared with anyone.
After this we have to create a folder named “faces” in the firebase storage, also we have to create two collections in Firebase Firestore with the exact names “classes” and “students”.

##### Camera Requirements:
In case a camera is connected to the machine running the program then one should make sure to make the required camera as the default camera which would take the video feed, by default the laptop webcam is used for this purpose.

##### Final steps:
After all this preparation, double click the “FRwithWebcam.py” to run it. The webcam will soon start and any person whose encoding is present in the files shall be identified and his/her attendance will be marked in the Excel sheet of the class which is scheduled at that time. In case there are no scheduled classes at the time of execution, one can create a class on the fly by providing basic info, please note that you should provide correct start and end time of the class at this point as attendance for future classes will be marked in the Excel sheet of the class currently running at the time of execution.
How to terminate:
Press “q” to stop the program. All the excel sheets can be found in the “AttendanceSheets” folder.


## Screenshots


Detection and working of backend machine learning model

![Screenshot 2021-11-14 171017](https://user-images.githubusercontent.com/57047418/141684752-36e943fd-66e5-4682-b77f-a74864a37605.png)

