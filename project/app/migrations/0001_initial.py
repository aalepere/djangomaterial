# Generated by Django 2.2.3 on 2019-07-13 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input1', models.CharField(max_length=10)),
                ('input2', models.CharField(max_length=10)),
            ],
        ),
    ]