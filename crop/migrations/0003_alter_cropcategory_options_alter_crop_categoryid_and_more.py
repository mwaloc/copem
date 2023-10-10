# Generated by Django 4.2.6 on 2023-10-05 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0002_crop'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cropcategory',
            options={'verbose_name': 'Crop Category', 'verbose_name_plural': 'Crop Categories'},
        ),
        migrations.AlterField(
            model_name='crop',
            name='categoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crop.cropcategory', verbose_name='Crop Category'),
        ),
        migrations.CreateModel(
            name='PlantingCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantingDate', models.DateField(verbose_name='Planting Date')),
                ('expectedHarvestDate', models.DateField(verbose_name='Expected Harvest Date')),
                ('expectedHarvestAmount', models.CharField(max_length=50, verbose_name='Expected Harvest Date')),
                ('cropId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crop.crop')),
            ],
        ),
    ]
