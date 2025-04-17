from django.db import models
from PIL import Image
import os
import random


class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    thumbnail = models.ImageField(upload_to='gallery/thumbs/', editable=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        # Преоразмеряване на основното изображение
        max_width = 1600
        if img.width > max_width:
            w_percent = (max_width / float(img.width))
            h_size = int((float(img.height) * float(w_percent)))
            img = img.resize((max_width, h_size), Image.LANCZOS)
            img.save(self.image.path)

        # Създаване на thumbnail
        thumb_size = (400, 400)
        img.thumbnail(thumb_size)
        base, ext = os.path.splitext(os.path.basename(self.image.name))
        thumb_name = f"{base}_thumb.jpg"
        thumb_path = os.path.join('gallery/thumbs/', thumb_name)
        full_thumb_path = os.path.join(os.path.dirname(self.image.path), "thumbs", thumb_name)

        # Създаваме директория ако липсва
        os.makedirs(os.path.dirname(full_thumb_path), exist_ok=True)
        img.save(full_thumb_path, "JPEG")

        # Записваме относителен път
        self.thumbnail.name = thumb_path
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(update_fields=["thumbnail"])

    def __str__(self):
        return self.title or f"Image {self.pk}"


    @property
    def layout_class(self):
        try:
            with Image.open(self.image.path) as img:
                width, height = img.size
                ratio = height / width

                if ratio < 0.8:
                    row_class = "row-span-1"
                elif ratio < 1.2:
                    row_class = "row-span-2"
                elif ratio < 1.6:
                    row_class = "row-span-3"
                else:
                    row_class = "row-span-4"
        except Exception:
            row_class = "row-span-2"

        # Добавяме рандомизиран col-span (1 до 2)
        col_class = random.choice(["col-span-1", "col-span-2"])

        # По желание: добави леко разбъркване на реда с order
        order_class = f"order-{random.randint(1, 6)}"

        return f"{col_class} {row_class} {order_class}"