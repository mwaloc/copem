# Generated by Django 4.2.6 on 2023-10-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'), ('Prefer not to say', 'Prefer not to say')], max_length=50, verbose_name='Gender')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]
