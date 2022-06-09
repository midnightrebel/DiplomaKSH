# Generated by Django 4.0 on 2022-06-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_students_days_students_subject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='students',
            name='granted',
        ),
        migrations.AddField(
            model_name='groups',
            name='aud',
            field=models.CharField(default=306, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students',
            name='group',
            field=models.ManyToManyField(to='mainapp.Groups'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='day',
            field=models.CharField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота')], default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='students',
            name='days',
            field=models.CharField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота')], default='0', max_length=1),
        ),
    ]
