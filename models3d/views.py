from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Model3D
from .forms import Model3DForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from orders.models import Order

@login_required
def my_models_view(request):
    user_models = Model3D.objects.filter(user=request.user).order_by("-created_at")

    model_prices = {}
    for model in user_models:
        order = (
            Order.objects.filter(model=model, price__isnull=False)
            .order_by("-created_at")
            .first()
        )
        if order:
            model_prices[model.id] = order.price

    return render(
        request,
        "models3d/my_models.html",
        {
            "models": user_models,
            "model_prices": model_prices,
        },
    )


@login_required
def upload_model_view(request):
    if request.method == "POST":
        form = Model3DForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.save()
            messages.success(request, "Моделът беше качен успешно!")
            return redirect("models3d:my_models")
    else:
        form = Model3DForm()

    return render(request, "models3d/upload_model.html", {"form": form})


@login_required
def edit_model_view(request, pk):
    model = get_object_or_404(Model3D, pk=pk, user=request.user)

    if request.method == "POST":
        form = Model3DForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
            messages.success(request, "Моделът беше обновен успешно.")
            return redirect("models3d:my_models")
    else:
        form = Model3DForm(instance=model)

    return render(request, "models3d/upload_model.html", {"form": form})


@login_required
def delete_model_view(request, pk):
    model = get_object_or_404(Model3D, pk=pk, user=request.user)

    if request.method == "POST":
        model.delete()
        messages.success(request, "Моделът беше изтрит успешно.")
        return redirect("models3d:my_models")

    return render(request, "models3d/confirm_delete.html", {"model": model})
