from django.shortcuts import render,redirect
from os import listdir
from os.path import isfile, join
import os
import cv2
# import dlib
import numpy as np
# import face_recognition
from django.views.generic import View
from .models import *
from imutils.video import FileVideoStream
from django.http.response import StreamingHttpResponse
import time
from imutils.video import FPS
import imutils
import cv2,os,urllib.request,pickle
# trackers = cv2.legacy.MultiTracker_create()

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
        # self.path = f'{self.BASE_DIR}video/'
        self.OPENCV_OBJECT_TRACKERS = {
            "csrt": cv2.TrackerCSRT_create(),
            "kcf": cv2.TrackerKCF_create(),
            # "boosting": cv2.TrackerBoosting_create(),
            "mil": cv2.TrackerMIL_create(),
            # "tld": cv2.TrackerTLD_create(),
            # "medianflow": cv2.TrackerMedianFlow_create(),
            # "mosse": cv2.TrackerMOSSE_create
        }
        images = []
        # self.trackers =self.OPENCV_OBJECT_TRACKERS["csrt"]
        self.classNames = []
        # self.myList = os.listdir(self.path)
        self.username = request.user.username
        self.repeate_name = []
        self.video = Video.objects.get().video
        self.trackers = self.OPENCV_OBJECT_TRACKERS['csrt']
        # self.cap = cv2.VideoCapture(f'{video}')

        # for cl in self.myList:
        #     curImg = cv2.imread(f'{self.path}/{cl}')
        #     images.append(curImg)
        #     self.classNames.append(os.path.splitext(cl)[0])

        # print(self.classNames)
        print(f'{self.BASE_DIR}{self.video}')
        self.vs = FileVideoStream(f'{self.BASE_DIR}/{self.video}').start()
        print(f'{self.BASE_DIR}/{self.video}')
        time.sleep(1.0)
        # start the FPS throughput estimator
        self.fps = FPS().start()


    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):
        while True:
            frame = self.vs.read()
            frame = cv2.flip(frame, 1)
            print(frame .shape)
            # resize the frame to have a width of 600 pixels (while
            # maintaining the aspect ratio), and then grab the image
            # dimensions
            frame = imutils.resize(frame, width=600)
            (success, boxes) = self.trackers.update(frame)
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
            c = 1
            trackers =self.OPENCV_OBJECT_TRACKERS["csrt"]
            while True:

            # img = captureScreen()
                imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
                imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                # grab the current frame, then handle if we are using a
                    # VideoStream or VideoCapture object
                
                # frame = frame[1] 
                # if args.get("video", False) else frame

                # check to see if we have reached the end of the stream
                if frame is None:
                    break

                # resize the frame (so we can process it faster)
                # frame = imutils.resize(frame, width=600)
                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # frame = np.dstack([frame, frame, frame])
                # grab the updated bounding box coordinates (if any) for each
                # object that is being tracked

                

                # loop over the bounding boxes and draw then on the frame
                for box in boxes:
                    (x, y, w, h) = [int(v) for v in box]
                    cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)

                # # show the output frame
                # cv2.imshow("Frame", frame)
                # # cv2.waitKey(100)
                # key = cv2.waitKey(1) & 0xFF

                # if the 's' key is selected, we are going to "select" a bounding
                # box to track
                if c==804:
                    # select the bounding box of the object we want to track (make
                    # sure you press ENTER or SPACE after selecting the ROI)q
                    # box = cv2.selectROI("Frame", frame, fromCenter=False,
                    #   showCrosshair=True)
                    # print(box)
                    # box = (838,253,993,409)
                    box = (66,94,122,140)
                    # create a new object tracker for the bounding box and add it
                    # to our multi-object tracker
                    # tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()
                    tracker = self.OPENCV_OBJECT_TRACKERS['kcf']
                    self.trackers.add(self.tracker, frame, box)
                
                # if the `q` key was pressed, break from the loop
                # elif key == ord("q"):
                #     break
                c = c+1
            # if we are using a webcam, release the pointer
            # if not args.get("video", False):
            #   vs.stop()

            # otherwise, release the file pointer
            # else:
            #     vs.release()

            # close all windows
            # cv2.destroyAllWindows()



            self.fps.update()
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

def track(request):
    return render(request, 'face-detection-update.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def facecam_feed(request):
    return StreamingHttpResponse(gen(Tracking(request)),
                                 content_type='multipart/x-mixed-replace; boundary=frame')