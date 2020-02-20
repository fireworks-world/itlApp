# Generated by Django 2.2.2 on 2020-02-20 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTable',
            fields=[
                ('articleID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('articleImage', models.ImageField(upload_to='image/')),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=34)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=10)),
                ('altPhone', models.CharField(max_length=13)),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=45)),
                ('request', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yes', models.BooleanField()),
                ('no', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=10)),
                ('languages', models.CharField(max_length=50)),
                ('interested', models.CharField(max_length=50)),
                ('demo', models.BooleanField()),
                ('demoDate', models.DateField()),
                ('todayDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField()),
                ('articleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ArticleTable')),
            ],
        ),
    ]
