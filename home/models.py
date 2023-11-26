from django.db import models

class Hostel(models.Model):
    name = models.CharField(max_length=255)
    vacancy = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    phone = models.CharField(max_length=15,default="nil")  # Adjust the max_length as needed
    mess_availability = models.CharField(max_length=15, default="NO")
    distance_from_college = models.FloatField(max_length=15,default=0.0)

    def __str__(self):
        return self.name
