from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,
                                  blank=True,
                                  null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=100,
                                    blank=True,
                                    null=True)

    def __str__(self):
        return f"User:  {self.user.username}"