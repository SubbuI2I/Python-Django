# Generated by Django 4.2 on 2023-04-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='email',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.participant'),
        ),
    ]
