# Generated by Django 3.0.8 on 2020-07-30 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='zip',
            new_name='zipcode',
        ),
    ]