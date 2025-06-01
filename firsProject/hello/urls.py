from django.urls import path

from firsProject.hello import views

urlPatterns = [
   path('',views.home, name='home')
]