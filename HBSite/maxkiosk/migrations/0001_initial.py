# Generated by Django 2.0.3 on 2018-10-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kiosk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('type', models.SmallIntegerField(choices=[(0, 'Hop'), (1, 'Max'), (2, 'Bus Stop'), (3, 'Plate Park'), (4, 'NikeBike'), (5, 'PDX Park')])),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('phone', models.CharField(max_length=255)),
                ('hours', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
                ('type', models.SmallIntegerField(choices=[(0, 'Shelters'), (1, 'Basic Needs'), (2, 'Food and Meals'), (3, 'Healthcare'), (4, 'Transportation')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('pass_id', models.BigIntegerField(help_text='Serial number from hop pass (7 bytes)', primary_key=True, serialize=False)),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'M'), (1, 'F'), (2, 'X')])),
                ('birthdate', models.DateField(blank=True)),
                ('guardian', models.BooleanField()),
                ('limited_mobility', models.BooleanField()),
            ],
        ),
    ]