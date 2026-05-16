from django.db import models


class Supplier(models.Model):
    name    = models.CharField(max_length=100)
    phone   = models.CharField(max_length=15)
    email   = models.EmailField()
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    CATEGORY_CHOICES = [
        ('medicine',   'Medicine'),
        ('equipment',  'Equipment'),
        ('consumable', 'Consumable'),  # gloves, syringes, bandages
        ('other',      'Other'),
    ]

    UNIT_CHOICES = [
        ('tablet',  'Tablet'),
        ('bottle',  'Bottle'),
        ('box',     'Box'),
        ('piece',   'Piece'),
        ('ml',      'ML'),
        ('kg',      'KG'),
    ]

    name          = models.CharField(max_length=100)
    category      = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    unit          = models.CharField(max_length=20, choices=UNIT_CHOICES)
    quantity      = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10)  # alert when below this
    expiry_date   = models.DateField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    supplier      = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.get_unit_display()})"

    def is_low_stock(self):
        return self.quantity <= self.reorder_level

    class Meta:
        ordering = ['name']