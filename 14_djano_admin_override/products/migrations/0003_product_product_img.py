# Generated by Django 5.0 on 2023-12-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, default='default/a.png', null=True, upload_to='products'),
        ),
    ]
