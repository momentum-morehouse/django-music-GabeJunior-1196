# Generated by Django 3.0.8 on 2020-07-15 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('released', models.DateField()),
            ],
        ),
    ]
