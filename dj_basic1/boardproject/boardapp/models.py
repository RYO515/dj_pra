from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    snsimage = models.ImageField(upload_to='')
    good = models.IntegerField()
    read = models.IntegerField()
    readtext = models.TextField()

    def __str__(self):
        return self.title
