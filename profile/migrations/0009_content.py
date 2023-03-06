# Generated by Django 4.1.5 on 2023-02-08 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userrole_access_team'),
        ('profile', '0008_skilldescription_skilltitle_candidate_skill_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('datetimemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.datetimemixin')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=250, null=True)),
                ('illustrate', models.TextField(blank=True, null=True, verbose_name='Content')),
            ],
            bases=('accounts.datetimemixin',),
        ),
    ]