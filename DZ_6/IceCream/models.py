from django.db import models

# Create your models here.
class IceCream(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженые'

class IceCreamShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    icecreams = models.ManyToManyField(IceCream)     

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин мороженого'
        verbose_name_plural = 'Магазины мороженого'
        
