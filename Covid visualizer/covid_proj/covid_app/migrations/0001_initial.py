# Generated by Django 3.0.3 on 2020-08-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.CharField(max_length=255)),
                ('cases', models.BigIntegerField()),
            ],
        ),
    ]