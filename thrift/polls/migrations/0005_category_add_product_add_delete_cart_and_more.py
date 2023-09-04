# Generated by Django 4.1.2 on 2022-12-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_login_passwd_alter_login_uname'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25)),
                ('quantity', models.CharField(max_length=25)),
                ('size', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('product_desc', models.CharField(max_length=15, verbose_name='Product description')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='category_table',
        ),
        migrations.DeleteModel(
            name='order_details',
        ),
        migrations.DeleteModel(
            name='order_items',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AlterField(
            model_name='user',
            name='pin',
            field=models.IntegerField(),
        ),
    ]
