# Generated by Django 4.1 on 2023-05-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practitioners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioners',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Unknown', 'Unknown')], max_length=25),
        ),
    ]
