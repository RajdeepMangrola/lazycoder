# Generated by Django 3.0.8 on 2020-07-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200730_0933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AlterField(
            model_name='contact',
            name='zipcode',
            field=models.CharField(max_length=122),
        ),
    ]