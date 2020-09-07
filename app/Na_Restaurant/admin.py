from django.contrib import admin
from .models import Restaurant
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display =['restaurant_id', 'restaurant_name', 'latitude', 'longitude', 'restaurant_address']

admin.site.register(Restaurant, RestaurantAdmin)