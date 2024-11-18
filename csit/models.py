from django.db import models

# Create your models here.

class Csit_2080(models.Model):
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
        db_table = "csit2080"

    def __str__(self) -> str:
        return self.name

# Batch CSIT 2079

class Csit_2079(models.Model):
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
        db_table = "csit2079"

    def __str__(self) -> str:
        return self.name

# Bacth CSIT 2078

class Csit_2078(models.Model):
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
        db_table = "csit2078"

    def __str__(self) -> str:
        return self.name

# Bacth CSIT 2077

class Csit_2077(models.Model):
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
        db_table = "csit2077"

    def __str__(self) -> str:
        return self.name

