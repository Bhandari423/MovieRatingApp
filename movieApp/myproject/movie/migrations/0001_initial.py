# Generated by Django 3.1.1 on 2020-09-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('year', models.IntegerField()),
                ('votes', models.IntegerField()),
                ('kind', models.CharField(max_length=250)),
            ],
        ),
    ]
