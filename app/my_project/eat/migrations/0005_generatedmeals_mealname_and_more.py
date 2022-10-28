# Generated by Django 4.1.1 on 2022-10-25 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eat', '0004_alter_ingredient_calories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedMeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MealName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('time', models.CharField(choices=[('M', 'morning'), ('A', 'afternoon'), ('E', 'evening')], db_index=True, max_length=1)),
            ],
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='carbohydrates',
            new_name='carbs',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='meal_title',
        ),
        migrations.DeleteModel(
            name='MealTitle',
        ),
        migrations.AddField(
            model_name='generatedmeals',
            name='meal_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eat.mealname'),
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_name',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.DO_NOTHING, to='eat.mealname'),
            preserve_default=False,
        ),
    ]