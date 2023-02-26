from django.contrib import admin
from .models import Student




@admin.register(Student)
class Admin(admin.ModelAdmin):



