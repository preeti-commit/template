# Generated by Django 3.0.6 on 2021-05-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('salary', models.IntegerField(max_length=255)),
                ('deduction', models.CharField(max_length=200)),
                ('gross_pay', models.CharField(max_length=200)),
            ],
        ),
    ]