from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    desc = models.TextField(blank=True)
    grade = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name    
