from django.db import models

# Create your models here.

class Staff(models.Model):
    appt = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    add = models.CharField(max_length=50)
    citizen = models.CharField(max_length=40)
    mob = models.CharField(max_length=10)
    marital = models.CharField(max_length=15)

    class Meta:
        db_table = 'staff'

    def __str__(self) -> str:
        return self.appt

