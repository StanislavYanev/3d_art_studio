from django.urls import path
from .views import home
from django.views.generic import TemplateView


app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path("privacy-policy/", TemplateView.as_view(template_name="privacy_policy.html"), name="privacy_policy"),
    path("terms/", TemplateView.as_view(template_name="terms.html"), name="terms"),
]
