# Generated by Django 3.1.7 on 2021-03-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symp_cat', models.CharField(max_length=100, verbose_name='Категория симптома')),
                ('symptom_text', models.CharField(max_length=500, unique=True, verbose_name='Симптом')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100, unique=True, verbose_name='Специалист')),
                ('diseases', models.ManyToManyField(to='SDDDS.Symptom', verbose_name='Лечит')),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=200, unique=True, verbose_name='Название класса')),
                ('symptoms', models.ManyToManyField(to='SDDDS.Symptom', verbose_name='Возможный симптом')),
            ],
        ),
    ]
