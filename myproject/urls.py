"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from frontend.sitemaps import StaticViewSitemap, ProductSitemap, BlogSitemap


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('models3d/', include('models3d.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('blog/', include('blog.urls')),
    path("gallery/", include("gallery.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'blog': BlogSitemap,
}

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]