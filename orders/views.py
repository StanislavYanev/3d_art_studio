from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from .models import Order
from models3d.models import Model3D  
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

@login_required
def create_order(request, model_id):
    model_instance = get_object_or_404(Model3D, id=model_id, user=request.user)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.model = model_instance
            order.save()
            return redirect('orders:my_orders')  # ще създадем този view скоро
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {
        'form': form,
        'model': model_instance
    })

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).select_related('model').order_by('-created_at')
    return render(request, 'orders/my_orders.html', {
        'orders': orders
    })

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status == 'pending':
        order.status = 'canceled'
        order.save()
    
    return redirect('my_orders')