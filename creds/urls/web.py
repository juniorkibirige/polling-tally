from django.urls import path
from creds.views.web import login


urlpatterns = [
    path('', login, name='login')
]
