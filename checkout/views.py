from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail
from django.template.loader import render_to_string


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            print("work propperly")
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

            # Изпращане на имейл до клиента
            subject_client = "Вашата поръчка в 3D Print Studio"
            message_client = render_to_string(
                "emails/order_confirmation_client.html",
                {
                    "order": order,
                    "cart": cart,
                    
                },
            )
            send_mail(subject_client, message_client, None, [order.email])

            # Изпращане на имейл до екипа
            subject_staff = f"Нова поръчка от {order.first_name} {order.last_name}"
            message_staff = render_to_string(
                "emails/order_notification_staff.html", {"order": order}
            )
            send_mail(subject_staff, message_staff, None, ["youremail@example.com"])
            cart.clear()
            return render(request, "checkout/created.html", {"order": order})

        print(form.errors)
    else:
        form = OrderCreateForm()
    return render(request, "checkout/create.html", {"cart": cart, "form": form})
