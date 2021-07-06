# Generated by Django 3.2.3 on 2021-07-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructapp', '0001_initial'),
        ('users', '0007_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='enrollments',
            field=models.ManyToManyField(blank=True, related_name='course', to='instructapp.Course'),
        ),
    ]