# Generated by Django 5.1.4 on 2024-12-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_reviews_app', '0013_alter_commentmotorpasion_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticiadiferente',
            name='titulo',
            field=models.CharField(max_length=2255),
        ),
    ]