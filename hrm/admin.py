from django.contrib import admin

from .models import Level, Task, Employee, Career, Assignments, TimeRecording

# Register your models here.
admin.site.register(Level)
admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(Career)
admin.site.register(Assignments)
admin.site.register(TimeRecording)