from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('ajax/', views.ajax, name="ajax"),
    path('result/<mbti>', views.result, name='result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)