# Generated by Django 3.1.7 on 2021-02-23 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20210223_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='trueChoice',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default=1, max_length=20),
        ),
    ]
