from farmer.models import Farmer
from django.db import models

# Create your models here.
class InputCategory(models.Model):
    inputCategoryName= models.CharField(max_length=50, verbose_name='Category')

    def __str__(self):
        return self.inputCategoryName
    
    class Meta:
        verbose_name= 'Input Category'
        verbose_name_plural= 'Input Categories'

class InputSupplier(models.Model):
    inputSupplierName=models.CharField(max_length=50, verbose_name='Supplier')
    phone= models.CharField(max_length= 50, verbose_name='Phone')
    email= models.EmailField(max_length=254, verbose_name='Email')
    

    def __str__(self):
        return self.inputSupplierName
    
class InputSupply(models.Model):
    
    inputCategoryId= models.ForeignKey(InputCategory, on_delete=models.CASCADE, verbose_name='Category')
    supplier= models.ForeignKey(InputSupplier, on_delete=models.CASCADE, verbose_name='Supplier')
    quantitySupplied= models.CharField(max_length=50, verbose_name='Quantity Supplied')
    dispatchDate= models.DateField(verbose_name='Dispatch Date')

    def __str__(self):
        return self.supplier.inputSupplierName
    
    class Meta:
        verbose_name='Input Supply'
        verbose_name_plural='Input Supplies'

class InputDistribution(models.Model):
    inputSupply = models.ForeignKey(InputSupply, on_delete=models.CASCADE, verbose_name='Input Supply')
    farmer = models.ForeignKey('farmer.Farmer', on_delete=models.SET_DEFAULT,
                                 default=None, null=True, verbose_name='Farmer')
    representativeNationalId = models.CharField(max_length=50, verbose_name='Represntative National ID')
    dispatchedQuantity = models.CharField(max_length=50, verbose_name='Dispatched Quantity')

    def __str__(self):
        
        return self.farmer.farmerName
    
    class Meta:
        verbose_name='Input Distribution'

# class InputRequest(models.Model):
#     farmId= models.ForeignKey(Farm, on_delete=models.CASCADE)
#     inputCategoryId= models.ForeignKey(InputCategory, on_delete=models.CASCADE, verbose_name='Category')
#     quantityRequested= models.CharField(max_length=50, verbose_name='Quantity Requested')
#     percentagePaid= models.IntegerField(verbose_name='Percentage Paid')
