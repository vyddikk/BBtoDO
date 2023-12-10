# Generated by Django 5.0 on 2023-12-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Todo', 'Todo'), ('dode', 'Done')], default='Todo', max_length=10)),
            ],
        ),
    ]
