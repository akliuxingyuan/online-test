# Generated by Django 3.1.7 on 2021-04-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20210423_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='chapter',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='章节'),
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('1', 'easy'), ('2', 'general'), ('3', 'difficult')], max_length=10, verbose_name='等级'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionA',
            field=models.CharField(max_length=50, verbose_name='A选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionB',
            field=models.CharField(max_length=50, verbose_name='B选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionC',
            field=models.CharField(max_length=50, verbose_name='C选项'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionD',
            field=models.CharField(max_length=50, verbose_name='D选项'),
        ),
    ]