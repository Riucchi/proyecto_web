from django.urls import path
from app_coder import views

urlpatterns = [
    path('registro/', views.autor_create_view),
    path('index/', views.inicio)]