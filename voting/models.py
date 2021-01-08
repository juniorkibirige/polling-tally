from django.db import models
from django.auth.contrib import User


class BaseModel(models.Model):
    name = models.CharField(max_length=256)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-id']


class District(BaseModel):
    code = models.CharField(max_length=64, unique=True)
    boundary_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name + ' in ' + self.region + ' region'


class County(BaseModel):
    district = models.ForeignKey('District', on_delete=models.CASCADE)
    code = models.CharField(max_length=64, unique=True)
    boundary_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subcounty(BaseModel):
    county = models.ForeignKey('County', on_delete=models.CASCADE)
    code = models.CharField(max_length=64, unique=True)
    boundary_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Parish(BaseModel):
    subcounty = models.ForeignKey('Subcounty', on_delete=models.CASCADE)
    code = models.CharField(max_length=64, unique=True)
    boundary_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Pollingstation(BaseModel):
    county = models.ForeignKey('County', on_delete=models.CASCADE)
    total_voters = models.IntegerField(blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
