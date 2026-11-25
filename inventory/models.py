from django.db import models
from dealers.models import DealerProfile

class Inventory(models.Model):
    class CylinderType(models.TextChoices):
        DOMESTIC = 'DOMESTIC', 'domestic'
        COMMERCIAL = 'COMMERCIAL', 'Comercial'

    dealer = models.ForeignKey(
        DealerProfile,
        on_delete= models.CASCADE,
        related_name= 'inventory'
    )

    brand = models.CharField(max_length= 100)
    cylinder_type = models.CharField(
        max_length= 20,
        choices= CylinderType.choices
    )

    available_quantity = models.PositiveIntegerField(default=0)

    is_available = models.BooleanField(default= True)

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} - {self.cylinder_type}"

# Create your models here.
