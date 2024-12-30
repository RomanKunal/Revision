from django.contrib import admin
from .models import Feedback
# Register your models here.
from .models import Student
admin.site.register(Student)
admin.site.register(Feedback)
