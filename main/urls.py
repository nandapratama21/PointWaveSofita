from django.urls import path
#now import the views.py file into this code
from main.views import show_main, compile_code,register, upload_file

urlpatterns=[
    path('', show_main, name='show_main'),
    path('compiler', compile_code, name='compile_code'),
    path('register/', register, name='register'),
    path('upload_endpoint', upload_file, name ='upload_file')


]