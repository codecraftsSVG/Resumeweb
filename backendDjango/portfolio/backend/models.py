# backend/models.py

from django.db import models

class Visitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # Add other fields as needed
