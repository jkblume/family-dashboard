# Generated by Django 2.2.7 on 2019-11-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventstream', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
            ],
        ),
    ]