from django.db import models

# Create your models here.

class ItemList(models.Model):
    Category_name = models.CharField(max_length=50)


class Items(models.Model):
    item_name = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    category = models.ForeignKey(ItemList,related_name="name",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Items/')
    



class AboutUs(models.Model):
    description = models.TextField(blank=False)



class Feedback(models.Model):
    user_name = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    rating = models.IntegerField()
    


class BookTable(models.Model):
    user_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    total_person = models.IntegerField()
    booking_date = models.DateField()
