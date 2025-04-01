from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "first_name",
            "phone_number",
            "last_name",
            "email",
            "address",
            "postal_code",
            "city",
            'comment',
        ]
        labels = {
            "first_name": "Име",
            "last_name": "Фамилия",
            "email": "Имейл",
            "phone_number": "Телефонен номер",
            "address": "Адрес",
            "postal_code": "Пощенски код",
            "city": "Град",
            'comment': 'Бележки',
        }
