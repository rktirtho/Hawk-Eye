# Library imported

# This is a sample Python script.
import os
import cv2
import face_recognition
import numpy as np
import pyttsx3
from PIL import Image
from dbh_person_reg import AuthorizedDbHelper
from dbh_organization import OrganizationDbHelper
from dbh_permit_area import PermitAreaDbHelper, PermitArea
from dbh_monitoring import MonitoringDbHelper
from dbh_stranger import StrangerDbHelper


from threading import Thread
import time
# import json
# import requests


# if __name__ == '__main__':
#     print_hi('PyCharm')

# call_api = requests.get('http://127.0.0.1:8080/api/permitteds')
#
# json_data = json.loads(call_api.content)
# for data in json_data:
#     print(data['imageId'])

org_db_helper = OrganizationDbHelper()
# ============================== Face Recognition Part ==============================
cam_name = "5st Floor"
path = "images/auth"
images = []
faceList = list()
stranger_faceList = list()
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


# ================================ Load Stranger Image from directory=====================

image_path = "images/strangers"
stranger_images = []
stranger_faceList = list()
stranger_classNames = []
stranger_myList = os.listdir(image_path)

for s_cl in stranger_myList:
    curImg = cv2.imread(f'{image_path}/{s_cl}')
    stranger_images.append(curImg)
    print(s_cl)
    stranger_classNames.append(os.path.splitext(s_cl)[0])


auth_db_helper = AuthorizedDbHelper()
auth_users = auth_db_helper.find_all_details()
dbh_monitoring = MonitoringDbHelper()
dbh_stranger = StrangerDbHelper()

stranger_current_id=12



print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[16].id)  # changing index, changes voices. 1 for female
    engine.say(text)
    engine.runAndWait()


def monitor(person_id, loc, type):
    if name not in faceList:
        faceList.append(name)
        dbh_monitoring.add(person_id, area, type)


encodeListKnown = findEncodings(images)
encodeListUnknown = findEncodings(stranger_images)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 10)
dbh_per = PermitAreaDbHelper()

# this list contain all people those entered in this camera covered area


while True:
    success, img = cap.read()
    # Converted Readed image in 1/4 size
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(imgS)
    encodingOfCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    # this is for testing mode

    for encodeFace, faceLoc in zip(encodingOfCurFrame, facesCurFrame):
        maches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)
        # bfeee99df268942206391ade4160ed2f2804fd06

        # this condition would be true when the face is a face of registered person
        if maches[matchIndex]:
            name = classNames[matchIndex]
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            for data in auth_users:

                if name in data.get_image():
                    area = dbh_per.getAreaById(data.get_id())

                    if cam_name in area:
                        cv2.putText(img, data.get_name(), (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

                        cv2.putText(img, data.get_organization(), (x1 + 6, y2 + 10), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                                    (0, 255, 0), 1)
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        if name not in faceList:
                            faceList.append(name)
                            dbh_monitoring.add(data.get_id(), cam_name, 1)
                    else:
                        cv2.putText(img, data.get_name(), (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                                    (0, 255, 255),
                                    1)

                        # cv2.rectangle(img, (x1, y2 + 25), (x2, y2),  cv2.FILLED)
                        cv2.putText(img, data.get_organization(), (x1 + 6, y2 + 10), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                                    (0, 255, 255), 1)
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
                        if name not in faceList:
                            faceList.append(name)
                            dbh_monitoring.add(data.get_id(), cam_name, 0)
        else:
            # when the face is not registered
            maches = face_recognition.compare_faces(encodeListUnknown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListUnknown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if maches[matchIndex]:
                # if the person visited previous in this system
                name = stranger_classNames[matchIndex]
                person = dbh_stranger.get_stranger_by_image_id(name)

                if name not in stranger_faceList:
                    dbh_monitoring.add(person.get_id(), cam_name, -1)
                    stranger_faceList.append(name)

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 165, 255), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 165, 255), cv2.FILLED)
                cv2.putText(img, "visited".upper(), (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
            else:
                # if the person visited previous in this system
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

                crop_img = img[y1:y1 + (y2-y1), x1:x1 + (x2-x1)]
                print(x1,x2,y1,y2)
                im = Image.fromarray(crop_img)
                # im = im.crop(faceLoc)
                image_id = 'st' + str(stranger_current_id)
                im.save('images/strangers/'+image_id+'.jpg')
                dbh_stranger.add(stranger_current_id,image_id)
                stranger_current_id += 1


                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, "unknown".upper(), (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)


    print(faceList)
    cv2.imshow(cam_name, img)
    cv2.waitKey(1)

# login()


# em_dbh.insert()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


