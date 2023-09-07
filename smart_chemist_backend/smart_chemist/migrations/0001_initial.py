# Generated by Django 3.2 on 2023-01-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotatedPattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smarts', models.CharField(max_length=500)),
                ('trivial_name', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=256)),
            ],
        ),
    ]