from django.shortcuts import render,redirect
from os import listdir
from os.path import isfile, join
import os
import cv2
import dlib
import numpy as np
import face_recognition
from django.views.generic import View
from .models import *
from imutils.video import FileVideoStream
from django.http.response import StreamingHttpResponse

from imutils.video import FPS
import imutils
import cv2,os,urllib.request,pickle

image_path = "faces"
BASE_DIR = "http://127.0.0.1:8000/"
# Create your views here.
def home(request):
    if request.method == "POST":
        video = request.FILES['video']
        data = Video.objects.create(
            video = video
        )
        data.save()
        return redirect("track:videos")
    return render(request,'index.html')

def videos(request):
    # videos = {}
    # videos['videos'] = Video.objects.all()
    path = f'video/faces/'
    print(path)
    images = []
    classNames = []
    newFile = []
    myList = os.listdir(path)
    for cl in myList:
        images.append(cl)
    classNames.append(os.path.splitext(cl)[0])
    videos = {'images':images,'classname':classNames}
    return render(request, 'videos.html',videos)

class FaceExtraction(View):
    def get(self,request):
        video = Video.objects.get().video
        print(video)
        self.detector = dlib.get_frontal_face_detector()
        self.cap = cv2.VideoCapture(f'{video}')
        # self.cap.set(cv2.CV_CAP_PROP_FPS, 20)
        self.img_size = 64
        self.margin = 0.2

        # Initialize Webcam
        frame_count = 0

        while True:
            ret, frame = self.cap.read()
            frame_count += 1

            input_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_h, img_w, _ = np.shape(input_img)
            detected = self.detector(frame, 1)
            faces = []
            if len(detected) > 0:
                for i, d in enumerate(detected):

                        x1, y1, x2, y2, w, h = d.left(), d.top(), d.right() + 1, d.bottom() + 1, d.width(), d.height()
                        xw1 = max(int(x1 - self.margin * w), 0)
                        yw1 = max(int(y1 - self.margin * h), 0)
                        xw2 = min(int(x2 + self.margin * w), img_w - 1)
                        yw2 = min(int(y2 + self.margin * h), img_h - 1)
                        face = frame[yw1:yw2 + 1, xw1:xw2 + 1, :]

                        file_name = "faces/" + str(frame_count) + "_" + str(i) + ".jpg"
                        cv2.imwrite(file_name, face)
        self.cap.release()
        return render(request,'loading_circle.html')

class Tracking(View):
    def __init__(self,request):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.path = 'faces/'

        images = []
        self.classNames = []
        self.myList = os.listdir(self.path)
        self.username = request.user.username
        self.repeate_name = []
        self.video = Video.objects.get().video

        # self.cap = cv2.VideoCapture(f'{video}')

        for cl in self.myList:
            curImg = cv2.imread(f'{self.path}/{cl}')
            images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])

        print(self.classNames)
        def findEncodings(images):
            encodeList = []

            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList

        self.encodeListKnown = findEncodings(images)
        self.vs = FileVideoStream(f'{self.video}').start()
        # start the FPS throughput estimator
        self.fps = FPS().start()


    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):

        frame = self.vs.read()
        frame = cv2.flip(frame, 1)

        # resize the frame to have a width of 600 pixels (while
        # maintaining the aspect ratio), and then grab the image
        # dimensions
        frame = imutils.resize(frame,width=600)
        (h, w) = frame.shape[:2]

        # # construct a blob from the image
        # imageBlob = cv2.dnn.blobFromImage(
        #     cv2.resize(frame, (300, 300)), 1.0, (300, 300),
        #     (104.0, 177.0, 123.0), swapRB=False, crop=False)

        # apply OpenCV's deep learning-based face detector to localize
        # faces in the input image
        # detector.setInput(imageBlob)
        # detections = detector.forward()

        # apply OpenCV's deep learning-based face detector to localize
        # faces in the input image
        repeate_name = []
        while True:

        # img = captureScreen()
            imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
        # print(faceDis)
                matchIndex = np.argmin(faceDis)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                if matches[matchIndex]:
                    name = self.classNames[matchIndex]
                    self.repeate_name.append(name)
        # print(name)

                    cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)



            self.fps.update()
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()




def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def track(request):
    return render(request, 'face-detection-update.html')

def facecam_feed(request):
    return StreamingHttpResponse(gen(Tracking(request)),
                                 content_type='multipart/x-mixed-replace; boundary=frame')