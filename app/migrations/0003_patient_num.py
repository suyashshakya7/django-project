# Generated by Django 4.2.2 on 2023-06-25 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_student_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
