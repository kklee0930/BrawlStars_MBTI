from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('question/', views.question, name='question'),
    path('ajax/', views.ajax, name="ajax"),
    path('result/', views.result, name='result'),
]
