from django.db import models

# Create your models here.
class Files(models.Model):
    changed_values = models.FileField(null=True)
    uniquevalues_one = models.FileField(null=True)
    uniquevalues_two = models.FileField(null=True)
    
class userInfo(models.Model):
    ip = models.GenericIPAddressField()
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.ip