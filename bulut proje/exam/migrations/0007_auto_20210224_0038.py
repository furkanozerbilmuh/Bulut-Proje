# Generated by Django 3.1.7 on 2021-02-23 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_auto_20210224_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='trueChoice',
            field=models.CharField(choices=[('A_choices', 'A'), ('B_choices', 'B'), ('C_choices', 'C'), ('D_choices', 'D'), ('E_choices', 'E')], default=1, max_length=20),
        ),
    ]
