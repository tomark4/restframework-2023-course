from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('find-us/', views.find_us, name="find_us"),
    path('contact/', views.contact, name="contact"),
    path('sample-page/', views.sample_page, name="sample_page"),
]
