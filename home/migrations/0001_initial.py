# Generated by Django 4.1.3 on 2022-11-10 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=408)),
                ('post', models.CharField(max_length=500)),
                ('comment', models.TextField()),
                ('image', models.TextField()),
            ],
        ),
    ]
