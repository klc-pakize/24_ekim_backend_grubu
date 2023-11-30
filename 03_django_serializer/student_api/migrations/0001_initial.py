# Generated by Django 4.2.7 on 2023-11-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=50)),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]
