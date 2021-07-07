from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'complete', 'create_date')
    list_display_links = ('title',)
    list_per_page = 10
    list_editable = ('complete',)


admin.site.register(Task, TaskAdmin)
