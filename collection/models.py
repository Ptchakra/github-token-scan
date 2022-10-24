from django.db import models

# Create your models here.

class GithubAccessToken(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    is_using = models.IntegerField()
    PURPOSES = (
        ('personal', 'Personal'),
        ('all', 'All'),
    )
    use_for_all = models.CharField(max_length=1, choices=PURPOSES, default='all')

