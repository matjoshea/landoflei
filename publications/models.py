from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Publication(models.Model):
    citation = models.TextField()
    title = models.CharField(max_length=300)
    pub_date = models.DateField()

    def __str__(self):
        return self.title
