# Generated by Django 4.2.7 on 2023-12-27 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='user',
        ),
        migrations.AlterField(
            model_name='habit',
            name='habit_owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
            preserve_default=False,
        ),
    ]
