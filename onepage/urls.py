from django.contrib import admin
from django.urls import path
from onepage import views
urlpatterns = [
    path('', views.index, name='index'),
    path('panel/',views.panel, name='panel'),
    path('login/',views.do_login, name='login'),
    path('logout/',views.do_logout, name='logout'),
    path('aboult/', views.add_aboult, name='aboult'),
    path('hero/', views.add_hero, name='hero'),
    path('hero/<int:hero_id>/', views.add_hero, name='edit_delete_hero'),
    path('produto/', views.add_produto, name='add_produto'),
    path('produto/<int:produto_id>/', views.add_produto, name='ac_produto'),
    path('categoria/', views.categoria, name='categoria'),
    path('message/', views.message, name='message'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<int:perfil_id>/', views.perfil, name='perfil_edit'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('testimonial/<int:testimonial_id>/', views.testimonial, name='del_edi_test'),
    path('testimonial-image/',views.image, name='image'),

]
