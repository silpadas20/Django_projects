from django.urls import path
from . import views

app_name= 'base'

urlpatterns =[
    path('',views.upload,name= 'getpoints'),
    path('download/',views.download,name='download'),
    path('export/',views.export,name='export'),
]
