# Generated by Django 4.2.6 on 2023-10-05 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('farm_size', models.CharField(max_length=50, verbose_name='Farm_Size')),
                ('farm_unit', models.IntegerField(choices=[('ac', 'Acre'), ('ha', 'Hectare')], max_length=256, verbose_name='Farm_Unit')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.farmer')),
            ],
        ),
    ]
