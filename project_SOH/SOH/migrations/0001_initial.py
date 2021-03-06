# Generated by Django 3.1.3 on 2020-11-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=10)),
                ('color', models.CharField(choices=[('RD', 'Red'), ('OR', 'Orange'), ('YL', 'Yellow'), ('YG', 'YellowGreen'), ('GN', 'Green'), ('SB', 'SkyBlue'), ('BL', 'Blue'), ('VT', 'Violet'), ('PK', 'Pink'), ('BK', 'Black'), ('GY', 'Gray'), ('WT', 'WHITE')], default='WT', max_length=2)),
                ('create_datetime', models.DateTimeField()),
                ('update_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('diary_no', models.IntegerField()),
                ('topic_no', models.IntegerField(default=0)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('datetime', models.DateTimeField()),
                ('emotion_score', models.IntegerField()),
                ('emotion_state', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=5)),
                ('age', models.IntegerField()),
                ('id', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
