# Generated by Django 3.0.6 on 2020-05-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidslapi', '0003_delete_districtcases'),
    ]

    operations = [
        migrations.CreateModel(
            name='districtCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bo', models.CharField(max_length=20)),
                ('Bonthe', models.CharField(max_length=20)),
                ('Bombali', models.CharField(max_length=20)),
                ('Falaba', models.CharField(max_length=20)),
                ('kailahun', models.CharField(max_length=20)),
                ('Kambia', models.CharField(max_length=20)),
                ('Karene', models.CharField(max_length=20)),
                ('Kono', models.CharField(max_length=20)),
                ('Kenema', models.CharField(max_length=20)),
                ('Koinadugu', models.CharField(max_length=20)),
                ('Moyamba', models.CharField(max_length=20)),
                ('Portloko', models.CharField(max_length=20)),
                ('Pujehun', models.CharField(max_length=20)),
                ('Tonkolili', models.CharField(max_length=20)),
                ('WesternRural', models.CharField(max_length=20)),
                ('WesternUrban', models.CharField(max_length=20)),
            ],
        ),
    ]
