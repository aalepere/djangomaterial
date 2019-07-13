from django.db import models

class Test(models.Model):
    input1 = models.CharField(max_length=10)
    input2 = models.CharField(max_length=10)
