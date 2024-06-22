from django.contrib import admin
from myapp.models import water



class myProd(admin.ModelAdmin):
    ist_display=["name" , "color" , "cost" ,"count" ,"volume"]
              
admin.site.register(water, myProd)
# Register your models here.
