from django.db import models

# Training Data Model
class TrainingData(models.Model):
    name=models.CharField(max_length=100)
    data_url=models.URLField(max_length=200,unique=True)
    
    def __str__(self):
        return self.name + " - " +self.data_url
