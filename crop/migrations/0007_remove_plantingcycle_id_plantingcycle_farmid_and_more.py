# Generated by Django 4.2.6 on 2023-10-06 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0009_remove_farm_farmunit_farm_farmer_farm_landunit_and_more'),
        ('crop', '0006_rename_name_cropcategory_cropcategoryname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantingcycle',
            name='id',
        ),
        migrations.AddField(
            model_name='plantingcycle',
            name='farmId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='farmer.farm', verbose_name='Farm Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plantingcycle',
            name='farmer_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farmer.farmer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plantingcycle',
            name='cropId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crop.cropcategory', verbose_name='Crop'),
        ),
    ]
