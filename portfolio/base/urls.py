from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('aboutme/', views.aboutme, name="aboutme"),
	path('certs/', views.certs, name="certs"),
	path('skills/', views.skills, name="skills"),
	path('contact/',views.contact, name='contact'),
	path('send_email/', views.sendEmail, name="send_email"),
    ]
