# Generated by Django 2.2.2 on 2019-07-09 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kariz', '0012_freelancer'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='teachingpermission',
            field=models.BooleanField(default=False),
        ),
    ]
