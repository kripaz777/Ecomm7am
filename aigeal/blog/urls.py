from django.urls import path,include
from .views import *

app_name = "blog"


urlpatterns = [
    path('', BlogView.as_view(),name = 'blog'),
    path('details/<slug>', BlogDetailsView.as_view(),name = 'details'),
    
]