# Generated by Django 3.2.6 on 2021-08-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamename', models.CharField(max_length=15)),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('elorating', models.IntegerField()),
                ('tournamentsplayed', models.IntegerField()),
                ('tournamentswon', models.IntegerField()),
                ('docfile', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
