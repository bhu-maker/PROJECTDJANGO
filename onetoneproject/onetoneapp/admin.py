from django.contrib import admin
from .models import Place,Restaurant,Waiter,Person,Project

# Register your models here.
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Project)
admin.site.register(Person)


#@admin.register(Place)
#class PlaceAdmin(admin.ModelAdmin):
#    list_display=['id','name','address']

#@admin.register(Restaurant)
#class PlaceAdmin(admin.ModelAdmin):
#    list_display=['place','server_hot_dogs','serves_pizza']