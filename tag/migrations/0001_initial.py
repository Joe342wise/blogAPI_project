# Generated by Django 5.0.6 on 2024-07-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TagTable',
            fields=[
                ('tagId', models.AutoField(db_column='tagID', primary_key=True, serialize=False)),
                ('tagName', models.CharField(db_column='tagName', max_length=50)),
            ],
            options={
                'db_table': 'tblTag',
            },
        ),
    ]
