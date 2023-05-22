from django.db import models


# Choices fields
MALE, FEMALE, OTHER, UNKNOWN = 'Male', 'Female', 'Other', 'Unknown'

# Defining Choices for Gender
GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
    (UNKNOWN, 'Unknown'),
]

# Create your models here.


class Practitioners(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField()
    telecom = models.IntegerField()
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    deceased = models.BooleanField()
    address = models.CharField(max_length=255)
    photo = models.ImageField()
