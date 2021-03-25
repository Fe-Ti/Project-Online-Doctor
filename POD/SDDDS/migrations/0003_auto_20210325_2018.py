# Generated by Django 3.1.7 on 2021-03-25 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SDDDS', '0002_auto_20210325_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Категория симптомов')),
            ],
        ),
        migrations.RemoveField(
            model_name='symptom',
            name='symp_cat',
        ),
        migrations.AddField(
            model_name='symptom',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SDDDS.category', verbose_name='Категория'),
        ),
    ]
