# Generated by Django 3.2.3 on 2021-06-30 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructapp', '0001_initial'),
        ('users', '0002_auto_20210629_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='enrollments',
            field=models.ManyToManyField(related_name='course', to='instructapp.Course'),
        ),
    ]
