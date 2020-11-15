# Library imported

# This is a sample Python script.
import os
import cv2
import face_recognition
import numpy as np
from dbh_person_reg import AuthorizedDbHelper
from dbh_organization import OrganizationDbHelper


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

path = "images/auth"
images = []
classNames = []
myList = os.listdir(path)

print(myList)
auth_db_helper =  AuthorizedDbHelper()
auth_users = auth_db_helper.find_all()

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
print('Encoding complete. Number of Register face:',len(encodeListKnown))

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    # Converted Readed image in 1/4 size
    imgS = cv2.resize(img,(0,0),None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(imgS)
    encodingOfCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc  in zip(encodingOfCurFrame, facesCurFrame):
        maches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if maches[matchIndex]:
            name = classNames[matchIndex]
            print(name)
            y1, x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4,y2*4,x1*4
            cv2.rectangle(img, (x1,y1),(x2,y2), (0,255,0), 2)

            for data in auth_users:
                if name in data[3]:
                    info = org_db_helper.find_one(data[0])
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, data[1] , (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

                    cv2.rectangle(img, (x1, y2 + 20), (x2, y2), (34, 255, 0), cv2.FILLED)
                    cv2.putText(img, info[1], ((x1 +x2)//2, y2 + 18), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)


            # for au in auth_users:
            #
            #     if name in au['name'].upper():
            #         if au['Auth'] == "Authorized":
            #             cv2.rectangle(img, (x1, y1 ), (x2, y1-35), (0, 255, 0), cv2.FILLED)
            #             cv2.putText(img, au['Auth'], (x1 + 6, y1-6 ), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            #         else:
            #             cv2.rectangle(img, (x1, y1), (x2, y1 - 35), (0, 0, 255), cv2.FILLED)
            #             cv2.putText(img, au['Auth'], (x1 + 6, y1 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
        else:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0,0,255), cv2.FILLED)
            cv2.putText(img, "unknown".upper(), (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


    cv2.imshow('Webcam', img)
    cv2.waitKey(1)





# login()


# em_dbh.insert()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
