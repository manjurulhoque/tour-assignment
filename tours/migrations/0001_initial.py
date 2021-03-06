# Generated by Django 3.0.6 on 2020-05-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('minimum_duration', models.DecimalField(decimal_places=2, max_digits=5)),
                ('locations', models.ManyToManyField(to='locations.Location')),
            ],
        ),
    ]
