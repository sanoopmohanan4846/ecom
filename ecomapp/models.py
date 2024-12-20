from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

# createing profile models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=10, blank=True)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    old_cart= models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
# for creating a user profile automatically when the user signup
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        
# automate the profile thing
post_save.connect(create_profile, sender=User)


# category model
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    



# customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    


# Product model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=400, null=True, blank=True, default='',)
    image = models.ImageField(upload_to='uploads/product/')
    rate = models.DecimalField(default=0, decimal_places=1, max_digits=7)
    # sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    
    def __str__(self):
        return self.name
    



# order model 
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(default='',blank=True, max_length=50)
    phone =models.CharField(default='', max_length=20, blank=20)
    date =models.DateField( default=datetime.datetime.today)
    status = models.BooleanField(default=False)