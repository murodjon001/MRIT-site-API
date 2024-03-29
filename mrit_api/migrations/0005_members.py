# Generated by Django 4.1.3 on 2022-11-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrit_api', '0004_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/photo_member')),
                ('telegram', models.URLField()),
                ('instagram', models.URLField()),
                ('facebook', models.URLField()),
                ('linkidin', models.URLField()),
                ('github', models.URLField()),
            ],
        ),
    ]
