# Generated by Django 3.0.8 on 2020-07-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('lastname', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('state', models.CharField(max_length=122)),
                ('zip', models.IntegerField(max_length=122)),
            ],
        ),
    ]
