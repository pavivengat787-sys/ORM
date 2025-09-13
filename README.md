# Ex02 Django ORM Web Application
## Date:13.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

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

admin.py

from django.contrib import admin
from .models import car_db,car_dbAdmin
admin.site.register(car_db,car_dbAdmin)
```


## OUTPUT

![alt text](<Screenshot (14).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
