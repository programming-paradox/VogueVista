# Generated by Django 5.0.6 on 2024-05-10 20:33

import Company.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='about_company',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=Company.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
