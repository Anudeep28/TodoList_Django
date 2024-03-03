from django.contrib import admin
from .models import TaskModel
# Register your models here.


# TO make changes how the data is displayed in admin
class TaskAdminView(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fields = ('task',)

admin.site.register(TaskModel,TaskAdminView)