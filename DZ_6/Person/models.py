from django.db import models

Male = 'М'
Female = 'Ж'
Genders = [
    (Male, 'Мужской'),
    (Female, 'Женский')
]

# Create your models here.
class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=Genders)
    
    def __str__(self):
        return self.first_name +'' + self.last_name

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'

class Child(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1,choices=Genders)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

