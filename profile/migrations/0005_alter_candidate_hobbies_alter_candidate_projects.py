# Generated by Django 4.1.5 on 2023-01-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_candidate_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='hobbies',
            field=models.ManyToManyField(blank=True, to='profile.hobby'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='projects',
            field=models.ManyToManyField(blank=True, to='profile.project'),
        ),
    ]
