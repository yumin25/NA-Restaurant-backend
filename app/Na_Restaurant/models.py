from django.db import models
from members.models import User
from django.utils import timezone


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=50, blank=False)
    restaurant_region = models.CharField(max_length=50, blank=False)
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

    def __str__(self):
        return self.menu_name


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

class Category(models.Model):
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    food_category = models.CharField(max_length=1, choices=food_categories, default='e')
    currency_category = models.CharField(max_length=1, choices=currency_categories, default='n')


class Review_Local(models.Model):
    review_local_id = models.AutoField(primary_key=True)
    review_local_user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_local_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    review_local_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review_local_title = models.CharField(max_length=50, blank=False)
    review_local_text = models.TextField()
    review_local_date =  models.DateTimeField(default=timezone.now)
    review_local_star = models.IntegerField(default=5)


class Review_Other(models.Model):
    review_other_id = models.AutoField(primary_key=True)
    review_other_user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_other_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    review_other_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review_other_title = models.CharField(max_length=50, blank=False)
    review_other_text = models.TextField()
    review_other_date =  models.DateTimeField(default=timezone.now)
    review_other_star = models.IntegerField(default=5)


class Franchise(models.Model):
    franchise_id = models.AutoField(primary_key=True)
    franchise_name = models.CharField(max_length=50, blank=False)