from django.contrib import admin
from django.urls import path
from onepage import views
urlpatterns = [
    path('', views.index, name='index'),
    path('panel/',views.panel, name='panel'),
    path('update/', views.update, name='update'),
    path('login/',views.do_login, name='login'),
    path('logout/',views.do_logout, name='logout'),
]
