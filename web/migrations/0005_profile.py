# Generated by Django 5.1.2 on 2024-10-17 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pic', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.user')),
            ],
        ),
    ]