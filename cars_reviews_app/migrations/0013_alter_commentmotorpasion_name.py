# Generated by Django 5.1.4 on 2024-12-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_reviews_app', '0012_commentimdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmotorpasion',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]