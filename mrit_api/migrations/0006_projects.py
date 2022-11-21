# Generated by Django 4.1.3 on 2022-11-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrit_api', '0005_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('images', models.ImageField(blank=True, null=True, upload_to='media')),
                ('project_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
