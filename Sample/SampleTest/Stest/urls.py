from django import views
from django.urls import path
from SampleTest import views

urlpatterns =[
    path('Stest/', views.Stest, name='Stest'),
    path('Stest/<str:pk>/', views.Stest, name='Stest'),
]