# Generated by Django 5.0.6 on 2024-06-03 20:42

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrelas', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'A avaliação não pode ser inferior a 0 estrelas.'), django.core.validators.MaxValueValidator(5, 'A avaliação não pode ser superior a 5 estrelas.')])),
                ('comentario', models.TextField(blank=True, null=True)),
                ('filme_review', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='filmes.filme')),
            ],
        ),
    ]
