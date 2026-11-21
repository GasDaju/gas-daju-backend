from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(unique=True)

    class Role(models.TextChoices):
        CUSTOMER = 'CUSTOMER', 'Customer'
        DEALER = 'DEALER', 'Dealer'
        BUSINESS = 'BUSINESS', 'Business'

    role = models.CharField(
            max_length = 20,
            choices =Role.choices,
            default =Role.CUSTOMER
        )

    phone_number = models.CharField(
            max_length= 15,
            unique= True,
        )
    def __str__(self):
            return f"{self.username} ({self.role})"