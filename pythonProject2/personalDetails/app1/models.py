from django.db import models


class Details(models.Model):
    name = models.CharField(max_length=200)
    phn_num=models.CharField(max_length=10)
    aadhar_num=models.CharField(max_length=12)
    pan_num=models.CharField(max_length=10)
    passport_num=models.CharField(max_length=8)



