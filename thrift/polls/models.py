from django.db import models


class login(models.Model):
    uname = models.CharField(max_length=50)
    passwd = models.CharField(max_length=25)
    User_type = models.CharField(max_length=10)


class user(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField("First name", max_length=50)
    lname = models.CharField("Last name", max_length=50)
    housename = models.CharField("House name",max_length=100)
    city = models.CharField("City",max_length=50)
    street = models.CharField("Street",max_length=40)
    phoneno = models.IntegerField()
    pin = models.IntegerField()
    email = models.EmailField("Email",max_length=30)



class product_add(models.Model):
    product_name = models.CharField(max_length=25)
    quantity = models.CharField(max_length=25)
    size = models.CharField(max_length=25)
    price = models.IntegerField()
    product_desc = models.CharField("Product description", max_length=15)
    image = models.ImageField("image", upload_to='image/')










