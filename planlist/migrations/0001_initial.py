# Generated by Django 3.2.21 on 2023-10-02 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=256)),
                ('planStartTime', models.DateTimeField()),
                ('planEndTime', models.DateTimeField()),
                ('realStartTime', models.DateTimeField()),
                ('realEndTime', models.DateTimeField()),
                ('planer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planlist.planer')),
            ],
        ),
    ]