from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    phone_number = models.CharField(
        max_length=12,
        null=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    purchase_number = models.IntegerField(null=True)

    # def __str__(self):
    #     return 'Profile for user {}'.format(self.user.username)