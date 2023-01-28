from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=30)
    create_date = models.DateTimeField('date create')

    def __str__(self):
        return self.city_name


class Retailer(models.Model):
    retailer_name = models.CharField(max_length=30)
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date create')

    def __str__(self):
        return self.retailer_name


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    create_date = models.DateTimeField('date create')

    def __str__(self):
        return self.product_name


class Client(models.Model):
    client_name = models.CharField(max_length=30)
    product = models.ManyToManyField(Product)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date create')

    def __str__(self):
        return self.client_name



