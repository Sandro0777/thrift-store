# Generated by Django 4.1.2 on 2022-10-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('quantity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='category_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('category_name', models.CharField(max_length=25, verbose_name='Category Name')),
                ('category_desc', models.CharField(max_length=100, verbose_name='Category description')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('userid', models.CharField(max_length=100, verbose_name='UserId')),
                ('uname', models.CharField(max_length=100, verbose_name='Username')),
                ('passwd', models.CharField(max_length=25, verbose_name='password')),
                ('User_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('total_price', models.IntegerField(verbose_name='total Price')),
                ('order_status', models.CharField(max_length=100, verbose_name='Order Status')),
            ],
        ),
        migrations.CreateModel(
            name='order_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_items_id', models.IntegerField()),
                ('order_details_id', models.CharField(max_length=100, verbose_name='Order Details')),
                ('product_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('category_id', models.IntegerField(verbose_name='Category Id')),
                ('category_desc', models.CharField(max_length=100, verbose_name='Category Description')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('fname', models.CharField(max_length=100, verbose_name='First name')),
                ('lname', models.CharField(max_length=100, verbose_name='Last name')),
                ('housename', models.CharField(max_length=100, verbose_name='House name')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('street', models.CharField(max_length=100, verbose_name='Street')),
                ('phoneno', models.IntegerField()),
                ('pin', models.IntegerField(verbose_name='Pin')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
        ),
    ]
