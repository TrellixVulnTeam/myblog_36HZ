# Generated by Django 2.1.8 on 2020-06-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crt_ts', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('upd_ts', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('username', models.CharField(max_length=12, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=12, verbose_name='密码')),
                ('avatar', models.ImageField(upload_to='', verbose_name='头像')),
                ('phone', models.PositiveSmallIntegerField(unique=True, verbose_name='手机号')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('note', models.TextField(verbose_name='说明')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user_info',
            },
        ),
    ]