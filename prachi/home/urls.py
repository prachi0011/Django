from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"), ##home function need to create in views.py
    path("education", views.education, name="education"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]