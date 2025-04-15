from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    accept_terms = forms.BooleanField(
        label='Съгласен съм с <a href="/terms/" target="_blank" class="underline text-indigo-600">Общите условия</a>',
        required=True,
        error_messages={
            "required": "Трябва да се съгласите с Общите условия, за да продължите.",
        },
    )

    class Meta:
        model = Order
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address",
            "city",
            "courier",
            "delivery_type",
            "delivery_details",
            "comment",
        ]
        labels = {
            "first_name": "Име",
            "last_name": "Фамилия",
            "email": "Имейл",
            "phone_number": "Телефонен номер",
            "address": "Адрес",
            "city": "Град",
            "courier": "Куриер",
            "delivery_type": "Тип доставка",
            "delivery_details": "Офис или адрес",
            "comment": "Бележки",
        }

        error_messages = {
            "first_name": {
                "required": "Моля, въведете име.",
            },
            "last_name": {
                "required": "Моля, въведете фамилия.",
            },
            "email": {
                "required": "Моля, въведете имейл адрес.",
                "invalid": "Моля, въведете валиден имейл.",
            },
            "phone_number": {
                "required": "Моля, въведете телефонен номер.",
            },
            "address": {
                "required": "Моля, въведете адрес за доставка.",
            },
            "city": {
                "required": "Моля, въведете град.",
            },
            "courier": {
                "required": "Моля, изберете куриер.",
            },
            "delivery_type": {
                "required": "Моля, изберете тип доставка.",
            },
            "delivery_details": {
                "required": "Моля, въведете офис или адрес.",
            },
        }

    def clean_accept_terms(self):
        accepted = self.cleaned_data.get("accept_terms")
        if not accepted:
            raise forms.ValidationError(
                "Моля, приемете Общите условия, за да продължите."
            )
        return accepted
