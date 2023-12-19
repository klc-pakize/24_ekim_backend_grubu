# Generated by Django 5.0 on 2023-12-19 17:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('title', models.CharField(choices=[('TeamLead', 'Team Lead'), ('MidLead', 'Mid Lead'), ('Junior', 'Junior')], default='Junior', max_length=10)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=10)),
                ('salary', models.PositiveIntegerField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('departman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personel.departman')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
