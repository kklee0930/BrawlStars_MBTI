from django.contrib import admin
from .models import Questions, Brawlers, Visitors

# Register your models here.
admin.site.register(Questions)
admin.site.register(Brawlers)
admin.site.register(Visitors)
