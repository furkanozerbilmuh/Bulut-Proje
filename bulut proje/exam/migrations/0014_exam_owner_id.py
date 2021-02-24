# Generated by Django 3.1.7 on 2021-02-24 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210223_0406'),
        ('exam', '0013_remove_exam_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='owner_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
    ]
