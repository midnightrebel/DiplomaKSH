# Generated by Django 4.0.1 on 2022-05-18 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_groups_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='admin_root',
            field=models.BooleanField(default=True),
        ),
    ]