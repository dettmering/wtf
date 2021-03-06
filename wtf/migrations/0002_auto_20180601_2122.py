# Generated by Django 2.0.6 on 2018-06-01 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wtf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='wtf',
            name='tags',
        ),
        migrations.AddField(
            model_name='wtf',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='wtf.Tag'),
        ),
    ]
