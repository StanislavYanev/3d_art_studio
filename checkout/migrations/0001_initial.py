# Generated by Django 5.2 on 2025-04-21 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Име')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Имейл')),
                ('postal_code', models.CharField(max_length=20, verbose_name='Пощенски код')),
                ('city', models.CharField(max_length=100, verbose_name='Град')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Телефонен номер')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('courier', models.CharField(choices=[('speedy', 'Speedy'), ('econt', 'Еконт')], default='speedy', max_length=20, verbose_name='Куриер')),
                ('delivery_type', models.CharField(choices=[('office', 'До офис'), ('address', 'До адрес')], default='office', max_length=20, verbose_name='Тип доставка')),
                ('delivery_details', models.CharField(max_length=255, verbose_name='Офис или адрес')),
                ('is_shipped', models.BooleanField(default=False, verbose_name='Изпратена доставка')),
                ('is_delivered', models.BooleanField(default=False, verbose_name='Получена доставка')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
