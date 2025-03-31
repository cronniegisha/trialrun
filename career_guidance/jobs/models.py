from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=100)
    posted_date = models.DateField()
    job_url = models.URLField()

    def __str__(self):
        return self.title
