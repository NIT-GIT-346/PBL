# Generated by Django 4.2.5 on 2025-05-18 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('usn', models.CharField(blank=True, max_length=20)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True)),
                ('email_notifications', models.BooleanField(default=True)),
                ('achievement_alerts', models.BooleanField(default=True)),
                ('profile_views', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=255)),
                ('usn', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('fatherName', models.CharField(max_length=255)),
                ('motherName', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('parentContact', models.CharField(max_length=15)),
                ('tenthPercentage', models.FloatField()),
                ('tenthSchool', models.CharField(max_length=255)),
                ('tenthBoard', models.CharField(max_length=100)),
                ('tenthYear', models.IntegerField()),
                ('pucPercentage', models.FloatField()),
                ('pucCollege', models.CharField(max_length=255)),
                ('pucBoard', models.CharField(max_length=100)),
                ('pucYear', models.IntegerField()),
                ('cgpa', models.FloatField()),
                ('sem1_sgpa', models.FloatField(blank=True, null=True)),
                ('sem2_sgpa', models.FloatField(blank=True, null=True)),
                ('sem3_sgpa', models.FloatField(blank=True, null=True)),
                ('sem4_sgpa', models.FloatField(blank=True, null=True)),
                ('sem5_sgpa', models.FloatField(blank=True, null=True)),
                ('sem6_sgpa', models.FloatField(blank=True, null=True)),
                ('sem7_sgpa', models.FloatField(blank=True, null=True)),
                ('sem8_sgpa', models.FloatField(blank=True, null=True)),
                ('skills', models.TextField()),
                ('certifications', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
