from django.db import models

# Create your models here.

class HeaderText(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 256)
    
    def __str__(self):
        return self.title 
    
class FurnitureText(models.Model):
    text = models.CharField(max_length = 100)

    def __str__(self):
        return self.text[:20]
    
class Product(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'images/product/')
    price = models.FloatField()

    def __str__(self):
        return self.name
    
class AboutUs(models.Model):
    title = models.CharField(max_length = 50)
    disc = models.CharField(max_length = 255)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'images/blog/')
    subject = models.CharField(max_length = 100)
    desc = models.TextField()
    data = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length = 50)
    img = models.ImageField(upload_to = 'images/review/')
    desc = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
