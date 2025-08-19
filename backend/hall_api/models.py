from django.db import models


class hall_Master(models.Model):
    Off_Code = models.CharField(max_length=10)
    Hall_Code = models.CharField( max_length=20)
    Hall_Name = models.CharField(max_length=50)
    DAY_SPOC_Name = models.CharField( max_length=20)
    NGT_SPOC_Name = models.CharField( max_length=20)
    Capacity = models.IntegerField()
    Table = models.IntegerField()
    Table = models.IntegerField()
    Chairs = models.IntegerField()
    White_Board = models.BooleanField()
    Video = models.BooleanField()
    Audio = models.BooleanField()
    Wifi = models.BooleanField()
    Others = models.CharField()


















