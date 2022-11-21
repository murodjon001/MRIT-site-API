# Generated by Django 4.1.3 on 2022-11-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrit_api', '0003_blogpostmodels_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=13)),
                ('text', models.TextField()),
            ],
        ),
    ]
