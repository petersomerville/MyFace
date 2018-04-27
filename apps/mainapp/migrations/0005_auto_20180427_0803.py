# Generated by Django 2.0.4 on 2018-04-27 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20180427_0713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_id',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='authored_posts', to='mainapp.User'),
        ),
    ]