# Generated by Django 3.2.9 on 2021-11-29 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board_body', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='board_body.categories'),
        ),
    ]
