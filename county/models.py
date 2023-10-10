from django.db import models

# Create your models here.

class County(models.Model):
    countyName = models.CharField(max_length=50, verbose_name='Name')
    population = models.IntegerField(verbose_name='Population')
    area = models.CharField(max_length=100, verbose_name='Area')

    def __str__(self):
        return self.countyName
    
    class Meta:
        verbose_name= 'County'
        verbose_name_plural= 'Counties'

class SubCounty(models.Model):
    subCountyName = models.CharField(max_length=50, verbose_name='Name')
    population = models.IntegerField(verbose_name='Population')
    area = models.CharField(max_length=100, verbose_name='Area')
    county=models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.subCountyName
    
    class Meta:
        verbose_name='Sub-County'
        verbose_name_plural='Sub-Counties'

class Ward(models.Model):
    wardName = models.CharField(max_length=50, verbose_name='Name')
    population = models.IntegerField(verbose_name='Population')
    area = models.CharField(max_length=100, verbose_name='Area')
    subCounty=models.ForeignKey(SubCounty, on_delete=models.CASCADE)

    def __str__(self):
        return self.wardName

class CommunityArea(models.Model):
    communityAreaName= models.CharField(max_length=50, verbose_name='Name')
    ward= models.ForeignKey(Ward, on_delete=models.CASCADE)

    def __str__(self):
        return self.communityAreaName
    
class Village(models.Model):
    villageName= models.CharField(max_length= 50, verbose_name='Name')
    communityArea= models.ForeignKey(CommunityArea, on_delete=models.CASCADE)

    def __str__(self):
        return self.villageName