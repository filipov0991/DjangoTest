# Generated by Django 4.2.1 on 2023-05-16 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=99)),
                ('last_name', models.CharField(max_length=99)),
                ('blood_type', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('unemployed', models.BooleanField()),
                ('married', models.BooleanField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Marriage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('person1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person1', to='Human.person')),
                ('person2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person2', to='Human.person')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('date', models.DateField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Human.person')),
            ],
        ),
    ]
