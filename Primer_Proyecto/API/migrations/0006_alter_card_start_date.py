# Generated by Django 5.1.2 on 2024-11-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_card_delete_project_delete_task_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
