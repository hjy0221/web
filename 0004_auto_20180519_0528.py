# Generated by Django 2.0.3 on 2018-05-18 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0003_auto_20180519_0514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='name',
            new_name='state',
        ),
    ]
