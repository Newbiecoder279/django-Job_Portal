from django.db import models

# Create your models here.

JOB_TYPE_CHOICES= (
    ('Internship', 'Internship'),
    ('Part-time','Part-time'),
    ('Full-time','Full-time')
)
JOB_LOCATION_CHOICES = (
    ('Remote','Remote'),
    ('On-site','On-site')
)
class PostJob(models.Model):
    title = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    job_type = models.CharField(choices=JOB_TYPE_CHOICES, max_length=15)
    job_location = models.CharField(choices=JOB_LOCATION_CHOICES, max_length=15)
    short_descrption = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title