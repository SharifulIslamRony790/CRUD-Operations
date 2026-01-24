from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'roll',
                    'address',
                    'description',
                    'school',
                    'addmission_date',
                    'is_active'
                    )
    search_fields = ('name',
                     'roll',
                     'Is_active')
