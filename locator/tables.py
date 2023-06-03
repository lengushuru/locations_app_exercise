from .models import Location

locations = Location.objects.all
for location in locations:
    print(location.name, location.status, location.parent.name)
