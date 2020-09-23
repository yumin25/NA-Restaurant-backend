from django.contrib import admin
from django.utils.html import format_html

from .models import Restaurant, My_Map, Menu, Category, Review_Local, Review_Other
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurant_id', 'restaurant_name', 'latitude', 'longitude', 'restaurant_region', 'restaurant_address', 'image_1', 'image_tag1', 'image_2', 'image_tag2']

    def image_tag1(self, obj):
        return format_html('<img src="../../../media/{}" width="50px;"/>'.format(obj.image_1))

    def image_tag2(self, obj):
        return format_html('<img src="../../../media/{}" width="50px;"/>'.format(obj.image_2))


class My_Map_Admin(admin.ModelAdmin):
    list_display = ['my_map_id', 'my_id', 'my_restaurant']


class Menu_Admin(admin.ModelAdmin):
    list_display = ['menu_id', 'menu_restaurant', 'menu_name', 'menu_price']


class Category_Admin(admin.ModelAdmin):
    list_display = ['restaurant', 'food_category', 'currency_category']

class Review_Local_Admin(admin.ModelAdmin):
    list_display = ['review_local_id', 'review_local_user', 'review_local_restaurant', 'review_local_menu', 'review_local_title', 'review_local_date', 'review_local_star', 'review_local_text']

class Review_Other_Admin(admin.ModelAdmin):
    list_display = ['review_other_id', 'review_other_user', 'review_other_restaurant', 'review_other_menu', 'review_other_title', 'review_other_date', 'review_other_star', 'review_other_text']

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(My_Map, My_Map_Admin)
admin.site.register(Menu, Menu_Admin)
admin.site.register(Category , Category_Admin)
admin.site.register(Review_Local , Review_Local_Admin)
admin.site.register(Review_Other , Review_Other_Admin)