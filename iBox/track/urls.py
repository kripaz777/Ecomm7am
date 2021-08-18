from django.contrib import admin
from django.urls import path
from .views1 import *
app_name = "track"
urlpatterns = [
    path('', home, name='home'),
    path('videos', videos, name='videos'),
    path('extract', FaceExtraction.as_view(), name='extract'),
    path('facetrack/', track, name='facetrack'),
    # path('facetrack/', Tracking.as_view(), name='facetrack'),
    path('facecam_feed', facecam_feed, name='facecam_feed'),

]