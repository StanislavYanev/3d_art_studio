from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart
from django.http import JsonResponse

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    
    # количество
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)

    # Ако е AJAX (от fetch)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_count': cart.count(), 
        })

    # Ако е нормално изпратена форма — класически redirect
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart:cart_detail')
