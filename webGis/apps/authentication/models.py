from django.db import models

class Roles(models.Model):
  nama = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
        db_table = "roles"
