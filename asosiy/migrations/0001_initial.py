# Generated by Django 3.2.16 on 2023-02-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('bajarilish_vaqti', models.DateField()),
                ('batafsil', models.TextField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
