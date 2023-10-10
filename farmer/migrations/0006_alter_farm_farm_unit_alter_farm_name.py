# Generated by Django 4.2.6 on 2023-10-05 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0005_alter_farm_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='farm_unit',
            field=models.IntegerField(choices=[('ac', 'Acres'), ('ha', 'Hectares')], verbose_name='Farm_Unit'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.farmer', verbose_name=''),
        ),
    ]
