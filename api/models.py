from django.db import models

# Create your models here.
class Details(models.Model):
    fname= models.CharField(max_length = 180)
    lname= models.CharField(max_length = 180)

    def __str__():
        return self.fname
