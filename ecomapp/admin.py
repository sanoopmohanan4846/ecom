from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)



# mixing Profile info and User info
class ProfileInline(admin.StackedInline):
    model = Profile
    
# for extending user model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["first_name", "username", "last_name", "email"]
    inlines = [ProfileInline]
    
# unregistering user
admin.site.unregister(User)

# re-register the user
admin.site.register(User, UserAdmin)
    