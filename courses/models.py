from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name
