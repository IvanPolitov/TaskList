from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'id') #какую инфу показывать в админке
    list_filter = ('id',) #слева поле фильтрации в данном случае по айдишнику
    fields = ['task', 'title',] #порядок показа в админке№

