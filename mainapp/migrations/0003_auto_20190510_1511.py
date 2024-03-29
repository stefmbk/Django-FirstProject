# Generated by Django 3.0.dev20190501095127 on 2019-05-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='motivLetter',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='application',
            name='studyLevel',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='job',
            name='industry',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='occupation',
            field=models.CharField(default='', max_length=200),
        ),
    ]
