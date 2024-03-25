from django.contrib import admin

from .models import Level, Task, Worker

# Register your models here.
admin.site.register(Level)
admin.site.register(Task)
admin.site.register(Worker)