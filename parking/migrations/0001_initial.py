# Generated by Django 2.2.4 on 2019-12-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('pos_x', models.IntegerField()),
                ('pos_y', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
