from django.test import TestCase
from .models import InventoryItem, Supplier
from datetime import date


class SupplierModelTest(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(
            name  = 'MedSupply Nepal',
            phone = '9841333333',       # ← phone not p_phone
            email = 'supply@med.com',
        )

    def test_supplier_created(self):
        self.assertEqual(self.supplier.name, 'MedSupply Nepal')

    def test_supplier_str(self):
        self.assertEqual(str(self.supplier), 'MedSupply Nepal')


class InventoryItemTest(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(
            name  = 'MedSupply Nepal',
            phone = '9841333333',
            email = 'supply@med.com',
        )
        self.item = InventoryItem.objects.create(
            name           = 'Paracetamol',
            category       = 'medicine',
            unit           = 'tablet',
            quantity       = 100,
            reorder_level  = 20,
            expiry_date    = date(2027, 1, 1),  # ← expiry_date is required
            price_per_unit = 5.00,
            supplier       = self.supplier,
        )
        self.low_item = InventoryItem.objects.create(
            name           = 'Gloves',
            category       = 'consumable',
            unit           = 'box',
            quantity       = 5,
            reorder_level  = 10,
            expiry_date    = date(2027, 1, 1),
            price_per_unit = 200.00,
        )

    def test_item_created(self):
        self.assertEqual(self.item.name, 'Paracetamol')
        self.assertEqual(self.item.quantity, 100)

    def test_item_str(self):
        self.assertIn('Paracetamol', str(self.item))

    def test_is_low_stock_false_when_above_reorder(self):
        self.assertFalse(self.item.is_low_stock())

    def test_is_low_stock_true_when_below_reorder(self):
        self.assertTrue(self.low_item.is_low_stock())

    def test_is_low_stock_true_when_equals_reorder(self):
        self.item.quantity = 20
        self.item.save()
        self.assertTrue(self.item.is_low_stock())

    def test_supplier_linked(self):
        self.assertEqual(self.item.supplier.name, 'MedSupply Nepal')