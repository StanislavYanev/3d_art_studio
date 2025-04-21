from django.core.management.base import BaseCommand
from products.models import Product, Category, Tag, ProductImage
from django.utils.text import slugify
from faker import Faker
from django.core.files import File
import random
import os

class Command(BaseCommand):
    help = "Зарежда тестови продукти, категории, тагове и снимки"

    def handle(self, *args, **kwargs):
        fake = Faker('bg_BG')

        # Папка с изображения
        image_dir = os.path.join('media', 'products')
        image_files = [
            f for f in os.listdir(image_dir)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        ]

        if not image_files:
            self.stdout.write(self.style.WARNING("⚠️  Няма изображения в media/products/. Пропуска добавяне на снимки."))

        # 1. Категории
        categories = []
        for name in ["Фигурки", "Прототипи", "Индустриални части"]:
            slug = slugify(name)
            category, _ = Category.objects.get_or_create(slug=slug, defaults={"name": name})
            categories.append(category)

        # 2. Тагове
        tags = []
        for tag_name in ["3D", "PLA", "ABS", "Гланц", "Тест"]:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)

        # 3. Продукти
        for i in range(20):
            name = fake.word().capitalize() + " " + fake.color_name()
            description = fake.paragraph(nb_sentences=3)
            price = round(random.uniform(15.00, 120.00), 2)
            category = random.choice(categories)
            in_stock = random.choice([True, False])
            rating = round(random.uniform(2.0, 5.0), 1)
            is_new = random.choice([True, False])

            product = Product.objects.create(
                name=name,
                name_en=name + " EN",
                description=description,
                description_en=fake.text(),
                price=price,
                in_stock=in_stock,
                rating=rating,
                is_new=is_new,
                category=category,
            )

            # Тагове
            selected_tags = random.sample(tags, k=random.randint(1, 3))
            product.tags.set(selected_tags)

            # Снимка
            if image_files:
                image_name = random.choice(image_files)
                image_path = os.path.join(image_dir, image_name)

                with open(image_path, 'rb') as img_file:
                    ProductImage.objects.create(
                        product=product,
                        image=File(img_file, name=image_name),
                        is_main=True
                    )

        self.stdout.write(self.style.SUCCESS("🎉 Заредени са 20 примерни продукта с тагове, категории и снимки!"))
