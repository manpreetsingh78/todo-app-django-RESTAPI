from django.contrib import admin
from api.models import ToDoList
# Register your models here.


@admin.register(ToDoList)
class Todo(admin.ModelAdmin):
    list_display = ['id','title','description','due_date','tags','status','created_at']


