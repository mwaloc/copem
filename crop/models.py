from django.db import models
from farmer.models import *
# Create your models here.
class CropCategory(models.Model):
    cropCategoryName= models.CharField(max_length=50, verbose_name='Crop Category')

    def __str__(self):
        return self.cropCategoryName
    
    class Meta:
        verbose_name= 'Crop Category'
        verbose_name_plural= 'Crop Categories'
    
class Crop(models.Model):
    cropName= models.CharField(max_length=50, verbose_name='Crop Name')
    categoryId= models.ForeignKey(CropCategory, on_delete=models.CASCADE, verbose_name='Crop Category')

    def __str__(self):
        return self.cropName

class PlantingCycle(Farmer):
    farmId= models.ForeignKey(Farm, on_delete=models.CASCADE, verbose_name= 'Farm Name')
    cropId= models.ForeignKey(Crop, on_delete=models.CASCADE, verbose_name='Crop')
    plantingDate= models.DateField(verbose_name='Planting Date')
    expectedHarvestDate= models.DateField(verbose_name='Expected Harvest Date')
    expectedHarvestAmount= models.CharField(max_length=50, verbose_name='Expected Harvest Amount')
    
    def __str__(self):
        return self.farmerName