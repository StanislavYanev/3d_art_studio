from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Име на продукта")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (лв.)")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name="Снимка")
    available = models.BooleanField(default=True, verbose_name="В наличност")

    def __str__(self):
        return self.name
