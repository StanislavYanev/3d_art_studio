from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/<int:model_id>/', views.create_order, name='create_order'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),

]
