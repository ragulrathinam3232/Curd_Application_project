# Generated by Django 5.1.2 on 2024-10-24 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=90)),
                ('Age', models.CharField(default='', max_length=90)),
                ('Notes', models.CharField(default='', max_length=90)),
            ],
        ),
    ]
