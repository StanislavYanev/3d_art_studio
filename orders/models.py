from django.db import models
from django.contrib.auth.models import User
from models3d.models import Model3D  

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Изчаква'),
        ('approved', 'Одобрена'),
        ('printing', 'Принтира се'),
        ('done', 'Завършена'),
        ('canceled', 'Отказана'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(Model3D, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
 
    def __str__(self):
        return f"{self.model} – {self.status} – {self.user}"
