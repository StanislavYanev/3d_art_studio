
from django.core.management.base import BaseCommand
from PIL import Image
import os
from gallery.models import GalleryImage
from django.conf import settings


class Command(BaseCommand):
    help = 'Генерира липсващи thumbnails за GalleryImage'

    def handle(self, *args, **kwargs):
        count = 0
        for image in GalleryImage.objects.all():
            if not image.thumbnail:
                try:
                    img_path = image.image.path
                    img = Image.open(img_path)
                    img.thumbnail((400, 400))

                    base, ext = os.path.splitext(os.path.basename(img_path))
                    thumb_name = f"{base}_thumb.jpg"
                    thumb_dir = os.path.join(settings.MEDIA_ROOT, 'gallery', 'thumbs')
                    os.makedirs(thumb_dir, exist_ok=True)
                    thumb_path = os.path.join(thumb_dir, thumb_name)

                    img.save(thumb_path, "JPEG")

                    # Записваме thumbnail пътя
                    image.thumbnail.name = f"gallery/thumbs/{thumb_name}"
                    image.save(update_fields=["thumbnail"])
                    count += 1
                    self.stdout.write(self.style.SUCCESS(f"✔ Генериран thumbnail за: {image.title or image.pk}"))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"✖ Грешка при {image.pk}: {e}"))
        self.stdout.write(self.style.SUCCESS(f"🎉 Готово! Обновени изображения: {count}"))
