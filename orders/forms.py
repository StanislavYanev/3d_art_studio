from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Напиши инструкции към поръчката...'
            }),
        }
        labels = {
            'comment': 'Инструкции / Бележка',
        }
