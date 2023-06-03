from django.db import models

class parent_loc(models.Model):
    name = models.CharField(max_length=255)


class Location(models.Model):
    parent = models.ForeignKey(parent_loc, on_delete=models.CASCADE,  null=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=100)

#explain this code

