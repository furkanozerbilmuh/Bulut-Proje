# Generated by Django 3.1.7 on 2021-02-24 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210223_0406'),
        ('exam', '0011_auto_20210224_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='owner_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='home.user'),
            preserve_default=False,
        ),
    ]