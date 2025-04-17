import random
from django.views.generic import ListView
from .models import GalleryImage
from django.views.generic import DetailView

class GalleryView(ListView):
    model = GalleryImage
    template_name = "gallery/gallery.html"
    context_object_name = "images"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = list(context["images"])
        styled_images = [{"image": img, "class": img.layout_class} for img in images]

        context["images"] = styled_images
        return context
    
    
class GalleryDetailView(DetailView):
    model = GalleryImage
    template_name = 'gallery/detail.html'
    context_object_name = 'image'