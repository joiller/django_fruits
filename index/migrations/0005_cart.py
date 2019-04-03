# Generated by Django 2.1.7 on 2019-03-31 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20190330_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Good')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
