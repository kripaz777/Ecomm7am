from django.urls import path,include
from .views import *

app_name = "company"


urlpatterns = [
    path('about/', About.as_view(),name = 'about'),
    path('carrer/', Carrer.as_view(),name = 'carrer'),
    path('apply/<slug>', CarrerDetails.as_view(),name = 'apply'),
    path('project/<slug>', ProjectDetail.as_view(),name = 'project'),
    path('product/<slug>', ProductDetail.as_view(),name = 'product'),
    path('solutions/', Solutions.as_view(),name = 'solutions'),

]