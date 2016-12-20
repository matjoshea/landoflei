from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    funding = models.CharField(max_length=200, blank=True)
    picture = models.FileField(blank=True)

    def __str__(self):
        return self.title
