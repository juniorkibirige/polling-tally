from django.urls import path
from creds.views.web import login, signup, reset_password


urlpatterns = [
    path('', login, name='login'),
    path('signup', signup, name='signup'),
    path('reset-password', reset_password, name="reset-password")
]
