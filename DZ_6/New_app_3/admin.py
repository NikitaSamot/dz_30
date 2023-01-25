from django.contrib import admin

# Register your models here.



from django.contrib import admin

# Register your models here.
from . models import Parent,Child


class ParentAdmin(admin.ModelAdmin):
    search_fields = ("first_name__startwith", "last_name__startwith",)

admin.site.register(Parent)
admin.site.register(Child)
