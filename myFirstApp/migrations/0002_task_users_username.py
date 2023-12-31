# Generated by Django 4.2.4 on 2023-08-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
