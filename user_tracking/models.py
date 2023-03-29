from django.db import models
from django.contrib.auth.models import User

class UserLoginLogout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField()
    
   
