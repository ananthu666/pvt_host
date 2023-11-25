from django.db import models

class Hostel(models.Model):
    name = models.CharField(max_length=255)
    vacancy = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

