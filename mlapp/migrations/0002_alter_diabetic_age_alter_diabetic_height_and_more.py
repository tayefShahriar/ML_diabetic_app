# Generated by Django 4.2.4 on 2023-08-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabetic',
            name='Age',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diabetic',
            name='Height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diabetic',
            name='Weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
