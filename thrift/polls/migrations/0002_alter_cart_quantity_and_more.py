# Generated by Django 4.1.2 on 2022-10-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category_table',
            name='category_desc',
            field=models.CharField(max_length=15, verbose_name='Category description'),
        ),
        migrations.AlterField(
            model_name='login',
            name='uname',
            field=models.CharField(max_length=50, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='login',
            name='userid',
            field=models.CharField(max_length=10, verbose_name='UserId'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category_desc',
            field=models.CharField(max_length=50, verbose_name='Category Description'),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=50, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=30, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(max_length=50, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(max_length=50, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='street',
            field=models.CharField(max_length=40, verbose_name='Street'),
        ),
    ]
