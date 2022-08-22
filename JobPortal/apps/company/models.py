from django.db import models
from ..account.models import User


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    designation = models.CharField(max_length=254, unique=True)
    description = models.CharField(max_length=254, null=True, blank=True)
    establishment_date = models.IntegerField(default=None, null=True, blank=True)
    website_url = models.URLField(max_length=254)
