from django.contrib import admin

from .models import Level, Task, Worker, Career, Assignments, TimeRecording

# Register your models here.
admin.site.register(Level)
admin.site.register(Task)
admin.site.register(Worker)
admin.site.register(Career)
admin.site.register(Assignments)
admin.site.register(TimeRecording)