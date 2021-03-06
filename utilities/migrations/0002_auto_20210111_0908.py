# Generated by Django 3.1.5 on 2021-01-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electricity',
            options={'verbose_name_plural': 'electricity'},
        ),
        migrations.AlterModelOptions(
            name='petrol',
            options={'verbose_name_plural': 'petrol'},
        ),
        migrations.AlterModelOptions(
            name='water',
            options={'verbose_name_plural': 'water'},
        ),
        migrations.AlterField(
            model_name='petrol',
            name='liters',
            field=models.DecimalField(decimal_places=2, help_text='How many liters did you fill up with?', max_digits=6),
        ),
    ]
