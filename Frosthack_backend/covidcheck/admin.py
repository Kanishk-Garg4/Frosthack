<<<<<<< HEAD
from django.contrib import admin
from .models import Check

# Register your models here.
class CheckAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_severe', 'other_symptoms']

admin.site.register(Check, CheckAdmin)
=======
from django.contrib import admin
from .models import Check

# Register your models here.
class CheckAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_severe', 'other_symptoms']

admin.site.register(Check, CheckAdmin)
>>>>>>> 4f9a23db109d44b3ab103c7713c1a1e3298d4a47
