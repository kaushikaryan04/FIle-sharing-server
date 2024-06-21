from django.urls import path 
from .views import UploadFileView , SignUpView , DownloadFileView
urlpatterns = [
    path('upload' , UploadFileView.as_view() ),
    path('signup' , SignUpView.as_view() ), 
    path('download' , DownloadFileView.as_view())
]