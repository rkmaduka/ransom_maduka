from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=300)
  email = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

