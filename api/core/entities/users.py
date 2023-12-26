from django.db import models;

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dni = models.CharField(max_length=8)
    cel_phone = models.CharField(max_length=9)
    address = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    image = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        