# Generated by Django 2.2.6 on 2019-10-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191022_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=225, unique=True),
        ),
    ]
