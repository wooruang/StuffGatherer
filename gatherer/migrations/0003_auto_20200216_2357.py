# Generated by Django 3.0.3 on 2020-02-16 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatherer', '0002_data_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='data',
            old_name='description',
            new_name='origin',
        ),
        migrations.AddField(
            model_name='data',
            name='category',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='sub_category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]