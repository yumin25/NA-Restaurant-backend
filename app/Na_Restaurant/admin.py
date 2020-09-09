from django.contrib import admin
from django.utils.html import format_html

from .models import Restaurant, My_Map
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurant_id', 'restaurant_name', 'latitude', 'longitude', 'restaurant_address', 'image_1', 'image_tag1', 'image_2', 'image_tag2']

    def image_tag1(self, obj):
        return format_html('<img src="../../../media/{}" width="50px;"/>'.format(obj.image_1))

    def image_tag2(self, obj):
        return format_html('<img src="../../../media/{}" width="50px;"/>'.format(obj.image_2))

class My_Map_Admin(admin.ModelAdmin):
    list_display = ['my_map_id', 'my_id', 'my_restaurant']


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(My_Map, My_Map_Admin)