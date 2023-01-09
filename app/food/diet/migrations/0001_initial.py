# Generated by Django 4.1.3 on 2022-11-13 12:09

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedMeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('calories', models.FloatField()),
                ('proteins', models.FloatField()),
                ('fats', models.FloatField()),
                ('carbs', models.FloatField()),
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
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.FloatField()),
                ('proteins', models.FloatField()),
                ('fats', models.FloatField()),
                ('carbs', models.FloatField()),
                ('gen_meals', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='diet.generatedmeals')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_weigth', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='diet.ingredient', verbose_name='ingredient')),
                ('meal_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='diet.mealname', verbose_name='meal_name')),
            ],
        ),
        migrations.AddField(
            model_name='generatedmeals',
            name='meal_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='diet.mealname'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[(0, 'FEMALE'), (1, 'MALE')], default=0, max_length=20, null=True)),
                ('target', models.CharField(blank=True, choices=[('L', 'LOSE'), ('S', 'STABLE'), ('G', 'GAIN')], max_length=1)),
                ('age', models.IntegerField(blank=True)),
                ('height', models.IntegerField(blank=True)),
                ('weight', models.IntegerField(blank=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('meal_plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='diet.mealplan')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
