# Generated by Django 3.1 on 2020-09-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_bookingjs'),
    ]

    operations = [
        migrations.CreateModel(
            name='consult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=20)),
            ],
        ),
    ]