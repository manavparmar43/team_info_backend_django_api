# Generated by Django 4.1.5 on 2023-01-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_company_description_candidate_experience_and_more'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrole',
            name='access_accept',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='access_team',
            field=models.ManyToManyField(to='profile.team'),
        ),
    ]