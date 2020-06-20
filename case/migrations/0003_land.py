# Generated by Django 3.0.2 on 2020-06-20 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_auto_20200620_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_number', models.CharField(max_length=100, verbose_name='地號')),
                ('land_url', models.CharField(max_length=100, verbose_name='地號謄本')),
                ('land_area', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='地坪')),
                ('land_holding_point_personal', models.PositiveSmallIntegerField(default=0)),
                ('land_holding_point_all', models.PositiveSmallIntegerField(default=0)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.Case', verbose_name='縣市')),
            ],
        ),
    ]
