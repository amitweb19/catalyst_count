# Generated by Django 4.2 on 2024-06-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('cid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=255)),
                ('year_founded', models.IntegerField(blank=True, null=True)),
                ('industry', models.CharField(max_length=255)),
                ('size_range', models.CharField(max_length=255)),
                ('locality', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('linkedin_url', models.URLField()),
                ('current_employee_estimate', models.IntegerField()),
                ('total_employee_estimate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CSVUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='csvs/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
