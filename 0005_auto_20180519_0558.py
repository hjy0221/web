# Generated by Django 2.0.3 on 2018-05-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0004_auto_20180519_0528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='state',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='code_number',
            field=models.IntegerField(default=1),
        ),
    ]
