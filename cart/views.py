from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def cart_detail(request):
    cart = Cart(request)
    is_mobile = "Mobile" in request.META.get("HTTP_USER_AGENT", "")

    return render(request, "cart/detail.html", {
        "cart": cart,
        "is_mobile": is_mobile,
    })


def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    
    quantity = int(request.POST.get('quantity', 1))
    personal_text = request.POST.get('personal_text', '')
    cart.add(product=product, quantity=quantity,personal_text=personal_text)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_count': cart.count(), 
        })

    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart:cart_detail')

@csrf_exempt
def update_cart_quantity(request, product_id):
    if request.method == "POST":
        data = json.loads(request.body)
        quantity = max(1, int(data.get("quantity", 1)))
        cart = Cart(request)
        cart.update(product_id=product_id, quantity=quantity)
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid method"}, status=405)