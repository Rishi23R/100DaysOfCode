# Generated by Django 4.2.7 on 2023-11-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phn_num', models.CharField(max_length=10)),
                ('aadhar_num', models.CharField(max_length=12)),
                ('pan_num', models.CharField(max_length=10)),
                ('passport_num', models.CharField(max_length=8)),
            ],
        ),
    ]