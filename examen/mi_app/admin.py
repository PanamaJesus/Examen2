from django.contrib import admin
from mi_app import models
# Register your models here.
@admin.register(models.Usery)
class UseryAdmin(admin.ModelAdmin):
    list_display=[
        'user_name'
    ]

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'description',
        'creator',
        'status'
    ]


