# Generated by Django 3.2.13 on 2022-11-29 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('opening_time', models.CharField(max_length=80)),
                ('break_day', models.CharField(max_length=80)),
                ('contact_number', models.CharField(max_length=80)),
                ('subtext', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hits', models.IntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0, null=True)),
            ],
        ),
    ]
