# Generated by Django 2.2.2 on 2020-02-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200220_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=50)),
                ('languages', models.CharField(max_length=80)),
            ],
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='no',
            new_name='option',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='yes',
        ),
    ]
