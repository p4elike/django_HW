from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=100)
    price = models.CharField(max_length=50)
    release_date = models.DateField()
    lte_exists = models.BooleanField(max_length=50)
    slug = models.SlugField(name)
    pass
