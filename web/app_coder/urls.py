from django.urls import path
from app_coder import views

urlpatterns = [
    path('index/', views.autor_create_view),]