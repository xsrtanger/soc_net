# Generated by Django 3.1.3 on 2020-12-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiler', '0002_auto_20201208_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='usernet',
            name='technology',
            field=models.ManyToManyField(related_name='users', to='profiler.Technology'),
        ),
    ]
