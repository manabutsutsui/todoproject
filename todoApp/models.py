from django.db import models

CHOICE = (('danger', 'high'), ('warning', 'normal'), ('primary', 'low'))

# Create your models here.
class todoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=CHOICE
        )
    dueDate = models.DateField()
    
    def __str__(self):
        return self.title