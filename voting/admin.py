from django.contrib import admin
from voting.models import (
    District, County, Subcounty, Parish, Pollingstation
)

# Register your models here.
appModels = [District, County, Subcounty, Parish, Pollingstation]
admin.site.register(appModels)
