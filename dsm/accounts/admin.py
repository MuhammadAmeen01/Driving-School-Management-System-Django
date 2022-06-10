from django.contrib import admin
from .models import customer, Teacher, attendance

# Register your models here.

admin.site.register(customer)
admin.site.register(Teacher)
admin.site.register(attendance)
