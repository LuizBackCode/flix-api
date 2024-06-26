# Generated by Django 5.0.6 on 2024-06-03 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='filme_review',
        ),
        migrations.AddField(
            model_name='review',
            name='filme',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='filme_review', to='filmes.filme'),
            preserve_default=False,
        ),
    ]
