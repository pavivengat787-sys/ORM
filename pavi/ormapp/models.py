from django.db import models
from django.contrib import admin
class car_db(models.Model):
     car_id=models.IntegerField(primary_key=True)
     brand=models.CharField(max_length=10)
     model_car=models.CharField(max_length=10)
     purchase_date=models.DateField()
     mileage=models.FloatField(default=0)
class car_dbAdmin(admin.ModelAdmin):
    list_display=["car_id","brand","model_car","purchase_date","mileage"]
