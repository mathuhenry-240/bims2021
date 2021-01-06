# Generated by Django 3.1.4 on 2021-01-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='phone_Number',
            new_name='Phone_Number',
        ),
        migrations.AddField(
            model_name='client',
            name='Acc_No',
            field=models.CharField(default=True, max_length=40),
        ),
        migrations.AddField(
            model_name='client',
            name='PoBox',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='client',
            name='Residence',
            field=models.CharField(default=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='client',
            name='Id_No',
            field=models.IntegerField(default=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Occupation',
            field=models.CharField(default=True, max_length=40),
        ),
    ]