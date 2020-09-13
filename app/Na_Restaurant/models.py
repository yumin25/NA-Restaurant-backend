from django.db import models
from members.models import User


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=50, blank=False)
    latitude = models.FloatField()
    longitude =models.FloatField()
    #grade = models.IntegerField(default=5)
    restaurant_address = models.CharField(max_length=50, null=True, blank=True)
    business_hours = models.CharField(max_length=50, null=True, blank=True)
    restaurant_phone = models.CharField(max_length=50, null=True, blank=True)
    image_1 = models.ImageField('image_1', upload_to = "restaurant/%Y/%m/%d", null=True, blank=True)
    image_2 = models.ImageField('image_2', upload_to= "restaurant/%Y/%m/%d", null=True, blank=True)


    def publish(self):
        self.save()

    def __str__(self):
        return self.restaurant_name

    def upload_to(instance, filename):
        return ""


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=50, blank=False)
    menu_price = models.CharField(max_length=50, blank=False)


class My_Map(models.Model):
    my_map_id = models.AutoField(primary_key=True)
    my_id = models.ForeignKey(User, on_delete=models.CASCADE)
    my_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


food_categories = (
    ('k', 'korean_food'),
    ('c', 'chinese_food'),
    ('j', 'japanese_food'),
    ('s', 'snack_food'),
    ('b' , 'bar'),
    ('w', 'western_food'),
    ('e', 'etc'),
)

currency_categories = (
    ('l', 'local_currency'),
    ('z', 'zero_pay'),
    ('n', 'nothing'),
)

class Categories(models.Model):
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    food_category = models.CharField(max_length=1, choices=food_categories, default='e')
    currency_category = models.CharField(max_length=1, choices=currency_categories, default='n')