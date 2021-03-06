# Generated by Django 3.1.7 on 2021-04-23 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20210423_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '选择题库', 'verbose_name_plural': '选择题库'},
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('AB', 'AB'), ('AC', 'AC'), ('AD', 'AD'), ('BC', 'BC'), ('BD', 'BD'), ('CD', 'CD'), ('ABC', 'ABC'), ('ABD', 'ABD'), ('BCD', 'BCD'), ('ABCD', 'ABCD')], max_length=10, verbose_name='答案'),
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('2', 'general'), ('3', 'difficult'), ('1', 'easy')], max_length=10, verbose_name='等级'),
        ),
    ]
