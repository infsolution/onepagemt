from django.contrib import admin
from django.urls import path
from onepage import views
urlpatterns = [
    path('', views.index, name='index'),
    path('panel/',views.panel, name='panel'),
    path('update/', views.update, name='update'),
    path('login/',views.do_login, name='login'),
    path('logout/',views.do_logout, name='logout'),
    path('aboult', views.add_aboult, name='aboult'),
    path('hero', views.add_hero, name='hero'),
    path('hero/<int:hero_id>', views.add_hero, name='edit_delete_hero'),

]
