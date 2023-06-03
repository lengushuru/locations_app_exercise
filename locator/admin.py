from django.contrib import admin
from .models import Location
from .models import parent_loc


admin.site.register(Location)
admin.site.register(parent_loc)


