from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.last_name


class Logger(models.Model):
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=4)
    query = models.CharField(max_length=200)
    body = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.method
