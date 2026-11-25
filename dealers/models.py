from django.db import models
from django.conf import settings

class DealerProfile(models.Model):
    user= models.OneToOneField(
        settings.AUTH_USER_MODEL    ,
        on_delete= models.CASCADE,
        related_name= 'dealer_profile'
    )

    shop_name = models.CharField(max_length= 150)
    owner_name= models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    latitude= models.DecimalField(max_digits= 9, decimal_places=6, null= True, blank=True)
    longitude= models.DecimalField(max_digits=9, decimal_places= 6, null= True, blank= True)
    registration_number = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.shop_name

# Create your models here.
