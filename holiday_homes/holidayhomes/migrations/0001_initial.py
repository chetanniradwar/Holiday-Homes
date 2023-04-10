# Generated by Django 4.2 on 2023-04-10 16:04

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HolidayHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_pictures', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), default=list, size=None)),
                ('length', models.PositiveSmallIntegerField()),
                ('width', models.PositiveSmallIntegerField()),
                ('rules', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), default=list, size=None)),
                ('address', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country_code', models.CharField(max_length=10)),
                ('primary_phone', models.PositiveBigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('country_of_residence', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_pictures', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), default=list, size=None)),
                ('room_type', models.CharField(choices=[('bed room', 'bed room'), ('kitchen', 'kitchen'), ('hall', 'hall'), ('bath_room', 'bath_room')], max_length=50)),
                ('length', models.PositiveSmallIntegerField()),
                ('width', models.PositiveSmallIntegerField()),
                ('holiday_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holidayhomes.holidayhome')),
            ],
        ),
        migrations.CreateModel(
            name='HomeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_for_24_hr_in_rupees', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('discount', models.PositiveIntegerField(default=0)),
                ('checkout_time', models.TimeField()),
                ('checkin_time', models.TimeField()),
                ('is_booked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('holiday_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holidayhomes.holidayhome')),
            ],
        ),
        migrations.AddField(
            model_name='holidayhome',
            name='owners',
            field=models.ManyToManyField(related_name='owners', to='holidayhomes.owner'),
        ),
    ]
