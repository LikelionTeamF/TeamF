# Generated by Django 4.1.7 on 2023-08-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0009_coinnews_source_name_coinnews_tickers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
