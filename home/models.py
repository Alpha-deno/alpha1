from django.db import models
from business.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from django.db.models import Q

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='propic')
    product_name = models.CharField(max_length=600)
    about_product = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()
    new = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    offer_price = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.product_image.path)
        if img.height > 300 and img.width > 300:
            output_size = (500, 775)
            img.thumbnail(output_size)
            img.save(self.product_image.path)
    def __str__(self):
        return self.product_name 
            
    '''def get_absolute_url(self):
        return reverse('home')'''
    


class Service(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    service_image = models.ImageField(upload_to='serpic')
    service_name = models.CharField(max_length=700)
    about_service = models.TextField(blank=True)
    price = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    new = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    offer_price = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.service_image.path)
        if img.height > 300 and img.width > 300:
            output_size = (500, 775)
            img.thumbnail(output_size)
            img.save(self.service_image.path)
    def __str__(self):
        return self.service_name
    '''def get_absolute_url(self):
        return reverse('home')'''


class Restaurant(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=255)
    food_image = models.ImageField(upload_to='fdpic')
    about_food = models.TextField(blank=True)
    price = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    offerprice = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.food_image.path)
        if img.height > 300 and img.width > 300:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.food_image.path)
    def __str__(self):
        return self.food_name
    '''def get_absolute_url(self):
        return reverse('home')'''

class BusinessActivator(models.Model):
    bussiness = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.BooleanField(default=False)
    date_activated = models.DateTimeField(default=timezone.now)
    service = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.bussiness.username} activated on {self.date_activated}'

class Contant(models.Model):
    Your_Name = models.CharField(max_length=255)
    Phone_Number = models.IntegerField(default=254)
    date_posted = models.DateTimeField(default=timezone.now)
    Subject = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
        return f'{self.Your_Name} {self.Subject}'

class OrderProduct(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    code = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=150)
    Phone_Number = models.IntegerField(default=254)
    product_1 = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    product_2 = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_2', blank=True)
    product_3 = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_3', blank=True)
    product_4 = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_4', blank=True)
    product_5 = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_5', blank=True)    
    product_6 = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_6', blank=True) 

class OrderFood(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    code = models.CharField(max_length=150)
    table_number = models.IntegerField(default=0)
    location = models.CharField(max_length=150)
    Phone_Number = models.IntegerField(default=254)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_1 = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    meal_2 = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='meal_2', blank=True)
    meal_3 = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='meal_3', blank=True)
    meal_4 = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='meal_4', blank=True)
    meal_5 = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='meal_5', blank=True)    
    meal_6 = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='meal_6', blank=True) 

class BookService(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    code = models.CharField(max_length=150)
    checkin_date = models.DateTimeField(default=timezone.now)
    Phone_Number = models.IntegerField(default=254)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    service_1 = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    service_2 = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='service_2', blank=True)
    service_3 = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='service_3', blank=True)
    service_4 = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='service_4', blank=True)
 




