# Generated by Django 5.1.6 on 2025-02-22 08:30

import django.db.models.deletion
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
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('course_id', models.IntegerField(unique=True)),
                ('course_name', models.CharField(max_length=500)),
                ('tuition_fees', models.CharField(blank=True, max_length=500, null=True)),
                ('beginning', models.CharField(blank=True, max_length=500, null=True)),
                ('subject', models.CharField(blank=True, max_length=500, null=True)),
                ('duration', models.CharField(blank=True, max_length=500, null=True)),
                ('languages', models.JSONField(default=list)),
                ('ielts_score', models.FloatField(blank=True, null=True)),
                ('toefl_score', models.FloatField(blank=True, null=True)),
                ('gmat_required', models.BooleanField(default=False)),
                ('gre_required', models.BooleanField(default=False)),
                ('gpa_requirement', models.FloatField(blank=True, null=True)),
                ('deadlines', models.JSONField(default=list)),
                ('application_link', models.URLField(blank=True, max_length=10000, null=True)),
                ('link_detail', models.URLField(blank=True, max_length=10000, null=True)),
                ('english_language_level', models.CharField(blank=True, max_length=500, null=True)),
                ('german_language_level', models.CharField(blank=True, max_length=500, null=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='programs.place')),
            ],
        ),
    ]
