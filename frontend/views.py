from django.shortcuts import render
from products.models import Product
import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import ContactMessage
from django.views.generic import TemplateView

def home(request):
    products = list(Product.objects.filter(in_stock=True))
    random.shuffle(products)
    featured_products = products[:4]

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Изпрати имейл
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            ContactMessage.objects.create(name=name, email=email, message=message)

            send_mail(
                subject=f"Ново съобщение от {name}",
                message=message + f"\n\nИмейл за връзка: {email}",
                from_email=None,
                recipient_list=[
                    "admin@3dprintstudio.bg"
                ],  # замени с реален имейл по-късно
            )
            messages.success(
                request, "✅ Благодарим! Съобщението беше изпратено успешно."
            )
            return redirect(
                "home:home"
            )  # можеш да пренасочиш към специална "благодарим" страница
    else:
        form = ContactForm()

    return render(
        request,
        "home.html",
        {
            "featured_products": featured_products,
            "form": form,
        },
    )


class AboutView(TemplateView):
    template_name = "about.html"