from django.urls import URLPattern
from django.urls import path
from . import views

app_name = 'imgUploader'

urlpatterns = [
    path('', views.imgUpload, name='Upload Images'),
    path("house/", views.House, name="House"),

    path("<str:pk>", views.page, name="page"),
    #path("")
]