from django.db import models
from practitioners.models import Practitioners

# Create your models here.


class Communications(models.Model):
    language = models.CharField(max_length=100)
    preffered = models.BooleanField()
    practitioner = models.ForeignKey(
        Practitioners, on_delete=models.CASCADE, related_name='communication')
