# Generated by Django 4.0.5 on 2022-06-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonnement',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='coach',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]