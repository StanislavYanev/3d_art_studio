from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.core.paginator import Paginator
from .forms import ProductImageForm

def product_list(request):
    products = Product.objects.all()
    
    # --- Филтриране ---
    category = request.GET.get('category')
    if category:
        products = products.filter(category__slug=category)

    price_min = request.GET.get('price_min')
    if price_min:
        products = products.filter(price__gte=price_min)

    price_max = request.GET.get('price_max')
    if price_max:
        products = products.filter(price__lte=price_max)

    sort = request.GET.get('sort')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')
    elif sort == 'latest':
        products = products.order_by('-created_at')

    # --- Пагинация ---
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj.object_list,
        'page_obj': page_obj,
        'categories': Category.objects.all(),
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            # можеш да пренасочиш, или да покажеш съобщение
    else:
        form = ProductImageForm(instance=product)

    return render(request, 'products/product_detail.html', {
        'product': product,
        'form': form,
    })

def upload_image(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')

    else:
        form = ProductImageForm(instance=product)

    return render(request, 'products/product_detail.html', {'form': form, 'product': product})