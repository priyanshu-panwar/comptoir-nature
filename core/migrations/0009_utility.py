# Generated by Django 2.2 on 2020-10-07 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Utilities',
            },
        ),
    ]
