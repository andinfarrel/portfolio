# Generated by Django 3.1 on 2020-08-28 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200825_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='full_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_snippet',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='project',
            name='text_snippet',
            field=models.CharField(max_length=20000),
        ),
    ]
