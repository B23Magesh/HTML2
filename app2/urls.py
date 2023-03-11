from django.urls import path
from app2.views import *
app_name='SAMPLE'
urlpatterns=[
    path('sample/',sample,name='sample')
]