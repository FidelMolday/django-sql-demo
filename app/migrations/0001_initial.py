# Generated by Django 5.0.2 on 2024-03-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('age', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=12)),
            ],
        ),
    ]
