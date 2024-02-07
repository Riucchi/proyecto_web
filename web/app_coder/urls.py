from django.urls import path
from app_coder import views

urlpatterns = [
    path('registro/', views.autor_create_view),
    path('index/', views.inicio, name="index"),
    path('about/',views.about, name="sobre nosotros"),
    path('booking/',views.booking, name="booking"),
    path('contact/',views.contact, name="contacto"),
    path('room/',views.room, name= "piezas"),
    path('service/',views.service, name="servicios"),
    path('team/',views.team, name="team"),
    path('testimonial/',views.testimonial,name="testimonio")
    ]