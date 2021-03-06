# Generated by Django 2.2 on 2022-03-08 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DB_userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wechat', models.CharField(default='', max_length=20)),
                ('sex', models.CharField(default='', max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('money', models.IntegerField(default=0)),
                ('adress', models.CharField(default='', max_length=20)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('appearance', models.IntegerField(default=0)),
                ('character', models.CharField(default='', max_length=20)),
                ('education', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DB_want',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(default=0)),
                ('money', models.IntegerField(default=0)),
                ('education', models.CharField(default='', max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('adress', models.CharField(default='', max_length=20)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to='myapp.DB_userInfo')),
            ],
        ),
    ]
