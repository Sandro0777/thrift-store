# Generated by Django 4.1.2 on 2022-12-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_category_add_product_add_delete_cart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_add',
            name='image',
            field=models.ImageField(default='a', upload_to='image/', verbose_name='photo'),
        ),
    ]
