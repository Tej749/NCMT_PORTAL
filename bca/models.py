from django.db import models
from django.shortcuts import render


# Create your models here.

# BCA 2080
class Bca_2080(models.Model):
    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=30)
    symbol = models.CharField(max_length=20)
    reg = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    add = models.CharField(max_length=60)
    guardian = models.CharField(max_length=50)
    prof = models.CharField(max_length=50)
    mobs = models.CharField(max_length=10)

    class Meta:
        db_table = "bca2080"

    def __str__(self) -> str:
        return self.name

# BCA 2079
class Bca_2079(models.Model):
    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=30)
    symbol = models.CharField(max_length=20)
    reg = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    add = models.CharField(max_length=60)
    guardian = models.CharField(max_length=50)
    prof = models.CharField(max_length=50)
    mobs = models.CharField(max_length=10)

    class Meta:
        db_table = "bca2079"

    def __str__(self) -> str:
        return self.name

# BCA 2078
class Bca_2078(models.Model):
    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=30)
    symbol = models.CharField(max_length=20)
    reg = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    add = models.CharField(max_length=60)
    guardian = models.CharField(max_length=50)
    prof = models.CharField(max_length=50)
    mobs = models.CharField(max_length=10)

    class Meta:
        db_table = "bca2078"

    def __str__(self) -> str:
        return self.name

# BCA 2077
class Bca_2077(models.Model):
    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=30)
    symbol = models.CharField(max_length=20)
    reg = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    add = models.CharField(max_length=60)
    guardian = models.CharField(max_length=50)
    prof = models.CharField(max_length=50)
    mobs = models.CharField(max_length=10)

    class Meta:
        db_table = "bca2077"

    def __str__(self) -> str:
        return self.name
