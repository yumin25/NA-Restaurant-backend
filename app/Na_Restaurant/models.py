from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=50, blank=False)
    latitude = models.FloatField()
    longitude =models.FloatField()
    #grade = models.IntegerField(default=5)
    restaurant_address = models.CharField(max_length=50, blank=True)
    business_hours = models.CharField(max_length=50, blank=True)
    restaurant_phone = models.CharField(max_length=50, blank=True)
    image_1 = models.ImageField('image_1', upload_to = restaurant_id, blank=True)
    image_2 = models.ImageField('image_2', upload_to= restaurant_id, blank=True)


    def publish(self):
        self.save()

    def __str__(self):
        return self.restaurant_name
