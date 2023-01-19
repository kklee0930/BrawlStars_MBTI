from django.contrib import admin
from .models import Questions, Choices

# Register your models here.
admin.site.register(Choices)
admin.site.register(Questions)