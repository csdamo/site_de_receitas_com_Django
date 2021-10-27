# Generated by Django 3.2.8 on 2021-10-22 13:59

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)
        ),
    ]