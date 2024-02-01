from django.urls import path
from app_coder import views

urlpatterns = [
    path('registro/', views.autor_create_view),
    path('index/', views.inicio),
    path('about/',views.about),
    path('booking/',views.booking),
    path('contact/',views.contact),
    path('room/',views.room),
    path('service/',views.service),
    path('team/',views.team),
    path('testimonial/',views.testimonial)
    ]