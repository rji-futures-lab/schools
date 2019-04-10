# Generated by Django 2.1.7 on 2019-03-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district_search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('school_year', models.IntegerField()),
                ('district_name', models.CharField(max_length=100)),
                ('enrollment_grades_k_12', models.IntegerField()),
                ('total_susp', models.IntegerField()),
                ('iss_b', models.IntegerField(null=True)),
                ('oss_b', models.IntegerField(null=True)),
                ('iss_w', models.IntegerField(null=True)),
                ('oss_w', models.IntegerField(null=True)),
                ('h', models.IntegerField(null=True)),
                ('a', models.IntegerField(null=True)),
                ('m', models.IntegerField(null=True)),
                ('p', models.IntegerField(null=True)),
                ('i', models.IntegerField(null=True)),
                ('b_disp', models.FloatField(null=True)),
                ('w_disp', models.FloatField(null=True)),
                ('h_disp', models.FloatField(null=True)),
                ('a_disp', models.FloatField(null=True)),
                ('m_disp', models.FloatField(null=True)),
                ('p_disp', models.FloatField(null=True)),
                ('i_disp', models.FloatField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='App',
        ),
    ]
