# Generated by Django 3.2.11 on 2022-01-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password2',
            field=models.CharField(max_length=50),
        ),
    ]