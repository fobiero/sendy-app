# Generated by Django 4.0.4 on 2022-04-17 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cost',
        ),
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='order.transportcost'),
            preserve_default=False,
        ),
    ]
