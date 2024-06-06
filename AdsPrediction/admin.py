from django.contrib import admin
from .models import TrainingData
# Register your models here.
@admin.register(TrainingData)
class TrainingDataAdmin(admin.ModelAdmin):
    list_display=['id','name','data_url']