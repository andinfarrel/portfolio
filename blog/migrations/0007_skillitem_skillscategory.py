# Generated by Django 3.1 on 2020-08-31 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SkillItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_text', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.skillscategory')),
            ],
        ),
    ]
