# Generated by Django 4.1.3 on 2023-02-01 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aadhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OTH', 'Others')], default='OTH', max_length=3)),
                ('aadhar_no', models.BigIntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
