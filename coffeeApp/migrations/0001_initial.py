# Generated by Django 4.0.3 on 2022-03-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeDrinker',
            fields=[
                ('userID', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'coffee_drinker',
            },
        ),
    ]
