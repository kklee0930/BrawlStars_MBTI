from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('question/<int:pk>', views.question, name='question'),
    path('result', views.result, name='result'),
]
