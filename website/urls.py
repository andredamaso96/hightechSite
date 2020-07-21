from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('contact.html', views.contact, name="contact"),
   path('about.html', views.about, name="about"),
   path('services.html', views.services, name="services"),
   path('oportunity.html', views.oportunity, name="oportunity"),
]
