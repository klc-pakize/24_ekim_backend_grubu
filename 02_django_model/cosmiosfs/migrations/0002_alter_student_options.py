# Generated by Django 4.2.7 on 2023-11-28 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cosmiosfs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-number'], 'verbose_name': 'Öğrenciler', 'verbose_name_plural': 'Öğrenci'},
        ),
    ]
