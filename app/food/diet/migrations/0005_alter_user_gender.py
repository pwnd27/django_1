# Generated by Django 4.1.3 on 2022-11-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0004_alter_user_meal_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, 'FEMALE'), (1, 'MALE')], default=0, null=True),
        ),
    ]
