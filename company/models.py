from django.db import models 
import uuid


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='company/profile_img')
    summary = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
