# Generated by Django 4.0.4 on 2022-06-13 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='ans',
            field=models.CharField(max_length=100, null=True),
        ),
    ]