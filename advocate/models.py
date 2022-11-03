from django.db import models 
import uuid

from company.models import Company


class Advocate(models.Model):
    username = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='advocate/profile_img')
    company = models.ForeignKey(Company, related_name='advocate', null=True, on_delete=models.CASCADE)
    short_bio = models.CharField(max_length=200)
    long_bio = models.TextField()
    twitter = models.CharField(max_length=200, null=True, blank=True)
    github = models.CharField(max_length=200, null=True, blank=True)
    advocate_years_of_experience = models.IntegerField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


