from django.db import models

# Create your models here.
class Farmer(models.Model):
    farmerName= models.CharField(max_length=50, verbose_name='Farmer Name')
    dob= models.DateField(verbose_name='Date of Birth')
    gender= models.CharField(max_length=50, verbose_name='Gender',
                              choices=[
                                  ('Male', 'Male'),
                                  ('Female','Female'),
                                  ('Transgender', 'Transgender'),
                                  ('Prefer not to say', 'Prefer not to say')
                              ])
    phone= models.CharField(max_length= 50, verbose_name='Phone')
    email= models.EmailField(max_length=254, verbose_name='Email')

    def __str__(self):
        return self.farmerName
    
class LandUnit(models.Model):
    landUnitName= models.CharField(max_length=50)
    landUnitAbbreviation= models.CharField(max_length=50)
    
    def __str__(self):
        return self.landUnitName


class Farm(models.Model):
    farmName= models.CharField(max_length=50, verbose_name=' Farm Name')
    farmer=models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farmSize= models.CharField(max_length=50, verbose_name='Farm Size')
    landUnit= models.ForeignKey(LandUnit, on_delete=models.CASCADE, verbose_name='Land Unit of Measure')

    def __str__(self):
        return self.farmName
    
