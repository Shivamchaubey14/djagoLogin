from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.IntegerField()

    class Meta:
        db_table = 'Inventory'

    def __str__(self):
        return self.name
