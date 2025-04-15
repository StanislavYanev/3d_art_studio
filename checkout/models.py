from django.db import models


class Order(models.Model):
    COURIER_CHOICES = [
        ("speedy", "Speedy"),
        ("econt", "Еконт"),
    ]

    DELIVERY_TYPE_CHOICES = [
        ("office", "До офис"),
        ("address", "До адрес"),
    ]

    first_name = models.CharField("Име", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Имейл")
    address = models.CharField("Адрес", max_length=250)
    postal_code = models.CharField("Пощенски код", max_length=20)
    city = models.CharField("Град", max_length=100)
    phone_number = models.CharField("Телефонен номер", max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True, null=True)
    courier = models.CharField("Куриер", max_length=20, choices=COURIER_CHOICES, default='speedy')
    delivery_type = models.CharField("Тип доставка", max_length=20, choices=DELIVERY_TYPE_CHOICES, default='office')
    delivery_details = models.CharField("Офис или адрес", max_length=255)
    


    def __str__(self):
        return f"Поръчка #{self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Количество", default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def get_cost(self):
        return self.price * self.quantity
