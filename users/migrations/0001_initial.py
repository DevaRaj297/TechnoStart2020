# Generated by Django 3.1 on 2020-08-08 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=50)),
                ('section', models.CharField(choices=[('sec1', 'SEC-1'), ('sec2', 'SEC-2'), ('sec3', 'SEC-3'), ('sec4', 'SEC-4')], max_length=10)),
                ('events', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
