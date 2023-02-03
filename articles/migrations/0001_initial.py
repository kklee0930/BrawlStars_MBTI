# Generated by Django 3.2.13 on 2023-01-18 17:06

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('I_choice', models.PositiveSmallIntegerField(default=0)),
                ('E_choice', models.PositiveSmallIntegerField(default=0)),
                ('S_choice', models.PositiveSmallIntegerField(default=0)),
                ('N_choice', models.PositiveSmallIntegerField(default=0)),
                ('T_choice', models.PositiveSmallIntegerField(default=0)),
                ('F_choice', models.PositiveSmallIntegerField(default=0)),
                ('P_choice', models.PositiveSmallIntegerField(default=0)),
                ('J_choice', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images')),
                ('question', models.TextField(max_length=200)),
                ('answer1', models.TextField(max_length=200)),
                ('answer2', models.TextField(max_length=200)),
            ],
        ),
    ]