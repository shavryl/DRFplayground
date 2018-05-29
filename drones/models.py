from django.db import models

# Create your models here.


class DroneCategory(models.Model):

    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name')

    def __str__(self):
        return self.name


class Drone(models.Model):

    name = models.CharField(max_length=250)
    drone_category = models.ForeignKey(
        DroneCategory, related_name='drones',
        on_delete=models.CASCADE)
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = 'name'

    def __str__(self):
        return self.name


