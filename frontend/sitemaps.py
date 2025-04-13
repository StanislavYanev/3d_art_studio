from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from products.models import Product
from blog.models import Article

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['home:home', 'products:product_list',]

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return reverse('products:product_detail', kwargs={'pk': obj.pk})
    

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Article.objects.filter(is_published=True)

    def location(self, obj):
        return reverse('blog:article_detail', kwargs={'slug': obj.slug})