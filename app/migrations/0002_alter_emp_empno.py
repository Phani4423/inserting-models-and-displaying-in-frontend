# Generated by Django 5.0.7 on 2024-10-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='empno',
            field=models.DecimalField(decimal_places=2, max_digits=7, primary_key=True, serialize=False),
        ),
    ]
