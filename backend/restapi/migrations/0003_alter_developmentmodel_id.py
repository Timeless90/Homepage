# Generated by Django 4.2.7 on 2023-11-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_developmentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developmentmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
