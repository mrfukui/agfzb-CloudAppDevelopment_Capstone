from django.contrib import admin
# from .models import related models
from .models import *

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display=["name", "dealer_id", "make", "year", "type"]

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display=["name", "description"]
    inlines=[CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.reigster(CarModel, CarModelAdmin)