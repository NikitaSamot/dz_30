from django.contrib import admin

# Register your models here.
from . models import IceCream, IceCreamShop
admin.site.register(IceCream)
admin.site.register(IceCreamShop)


