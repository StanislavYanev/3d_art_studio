from django.db import models
from django.contrib.auth.models import User

class Model3D(models.Model):
    CATEGORY_CHOICES = [
        ('prototype', 'Прототип'),
        ('figure', 'Фигурка'),
        ('mechanical', 'Механична част'),
        ('other', 'Друго'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='models3d')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    model_file = models.FileField(upload_to='3d_models/')
    preview_image = models.ImageField(upload_to='model_previews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
