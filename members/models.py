from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=200)
    new_employer = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    research_interests = models.TextField()
    picture = models.FileField(blank=True)

    def __str__(self):
        return self.last_name + ', ' + self.first_name


