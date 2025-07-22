from django.urls import path
from home.views import *
urlpatterns = [
    path('',home),
    path('successpage/',success_page),
]
