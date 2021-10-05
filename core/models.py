from django.db import models

# Create your models here.


class ItemGroup(models.Model):
    name = models.CharField(max_length=64, null=True)
    image = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Item(models.Model):
    item_group = models.ForeignKey(
        ItemGroup, null=True, on_delete=models.CASCADE, editable=True
    )
    name = models.CharField(max_length=64, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(max_length=300, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class AddOn(models.Model):
    name = models.CharField(max_length=64, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
