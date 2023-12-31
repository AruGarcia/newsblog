# Generated by Django 4.2.7 on 2023-12-10 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Business', 'Business'), ('Culture', 'Culture'), ('Food', 'Food')], default='Business', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default=None),
        ),
    ]
