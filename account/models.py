from django.contrib.auth.models import AbstractUser
from django.db import models
import random


class User(AbstractUser):
    date_of_birth = models.DateField('день рождения', blank=True, null=True)
    purchase_number = models.IntegerField('количество покупок', null=True)
    is_phone_number_verified = models.BooleanField('верификация', default=False)
    secret_user_token = models.CharField('токен подтверждения', max_length=6, null=True)
    a = [str(i) for i in range(0, 10)]

    def secret_token(self):
        tok = random.sample(User.a, 6)
        token = ''.join(tok)
        self.secret_user_token = token
        self.save()
        return token

    def send_token(self):
        token = self.secret_token()
        print(f'phone -->>  +{str(self.username)} , token -->> {token}')
        return

    def secret_token_valid(self, token):
        try:
            return token == self.secret_user_token
        except:
            return False

    def user_verify(self):
        self.is_phone_number_verified = True
        self.save()
        return

    def __str__(self):
        return self.username
