# Generated by Django 2.2 on 2019-09-11 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0002_auto_20190912_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies_list',
            name='movies_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
