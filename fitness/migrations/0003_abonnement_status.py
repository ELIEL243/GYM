# Generated by Django 4.0.5 on 2022-07-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0002_abonnement_date_alter_coach_name_alter_coach_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonnement',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]