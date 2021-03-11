from django.contrib import admin
from .models import Branch,Student,Subject,Attendance,Faculty

# Register your models here.
admin.site.register(Branch)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Faculty)

