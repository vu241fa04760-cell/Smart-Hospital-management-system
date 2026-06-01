from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=80, blank=True)
    manufacturer = models.CharField(max_length=120, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.stock_quantity})"
