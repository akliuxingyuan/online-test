# Generated by Django 3.1.7 on 2021-04-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20210421_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='examtime',
            new_name='exam_time',
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('2', 'general'), ('3', 'difficult'), ('1', 'easy')], max_length=10, verbose_name='等级'),
        ),
    ]
