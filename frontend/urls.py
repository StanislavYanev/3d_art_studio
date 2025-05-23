from django.urls import path
from .views import home
from django.views.generic import TemplateView
from .views import AboutView


app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path("privacy-policy/", TemplateView.as_view(template_name="privacy_policy.html"), name="privacy_policy"),
    path("terms/", TemplateView.as_view(template_name="terms.html"), name="terms"),
    path("about/", AboutView.as_view(), name="about"),
]
