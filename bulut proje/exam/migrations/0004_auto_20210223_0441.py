# Generated by Django 3.1.7 on 2021-02-23 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='A_choice',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='B_choice',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='C_choice',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='D_choice',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='E_choice',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=100),
        ),
    ]
