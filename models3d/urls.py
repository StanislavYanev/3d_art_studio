from django.urls import path
from . import views

app_name = 'models3d'

urlpatterns = [
    path('my-models/', views.my_models_view, name='my_models'),
    path('upload/', views.upload_model_view, name='upload_model'),
    path('<int:pk>/edit/', views.edit_model_view, name='edit_model'),
    path('<int:pk>/delete/', views.delete_model_view, name='delete_model'),
]
