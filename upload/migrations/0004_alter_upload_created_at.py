# Generated by Django 3.2.9 on 2021-11-17 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_remove_upload_n_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
