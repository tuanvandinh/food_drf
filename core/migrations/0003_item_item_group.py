# Generated by Django 3.2.7 on 2021-10-04 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_addon'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.itemgroup'),
        ),
    ]