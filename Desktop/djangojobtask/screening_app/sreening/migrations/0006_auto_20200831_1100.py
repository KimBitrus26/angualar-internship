# Generated by Django 3.1 on 2020-08-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sreening', '0005_auto_20200831_0435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='mark',
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(blank=True, help_text='Input option answere', max_length=800),
        ),
    ]