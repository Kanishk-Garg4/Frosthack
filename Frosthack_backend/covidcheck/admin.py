from django.contrib import admin
from .models import Check, PinCity

# Register your models here.
class CheckAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_severe', 'other_symptoms']

    fieldsets = [
        ('Registration Info', {'fields': ['name', 'phone', 'date']}),
        ('Covid Symptoms', {'fields': ['fever', 'cough', 'Tiredness', 'breathing_problem', 'chest_pain', '_other_symptoms' ]}),
    ]

    list_filter = ['date']

class PinCityAdmin(admin.ModelAdmin):
    list_display = ['name', 'locality', '_pin', 'city']

    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Address Information', {'fields': ['locality', 'city', '_pin']})
    ]

    list_filter = ['_pin']

admin.site.register(Check, CheckAdmin)
admin.site.register(PinCity, PinCityAdmin)
