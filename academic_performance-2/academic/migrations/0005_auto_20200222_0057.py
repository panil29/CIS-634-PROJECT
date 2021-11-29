# Generated by Django 3.0.3 on 2020-02-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_auto_20200221_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudent_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=10)),
                ('addr', models.TextField(default='DataFlair Address')),
            ],
        ),
        migrations.AlterField(
            model_name='addfaculty_model',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
