from django.contrib import admin
from django.urls import path
from onepage import views
urlpatterns = [
    path('recrutamento/', views.index, name='index'),
    path('update/', views.update, name='update'),
]
