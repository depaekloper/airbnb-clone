# Generated by Django 2.2.5 on 2021-03-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20210313_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='How many people will be staying?'),
        ),
    ]