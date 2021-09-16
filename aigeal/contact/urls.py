from django.urls import path,include
from .views import *

app_name = "Contact"


urlpatterns = [
    path('', ContactView.as_view(),name = 'contact'),
    path('contacts', contacts,name = 'contacts'),

]