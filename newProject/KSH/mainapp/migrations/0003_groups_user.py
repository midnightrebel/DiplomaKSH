# Generated by Django 4.0.4 on 2022-05-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_students_teachers_note_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameGroup', models.CharField(max_length=255)),
                ('day', models.DateTimeField()),
                ('max_count', models.IntegerField()),
                ('fact_count', models.IntegerField()),
                ('datestart', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('admin_root', models.BooleanField(default=False)),
            ],
        ),
    ]
