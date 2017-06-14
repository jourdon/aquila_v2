# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Privileges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_obj', models.CharField(max_length=50)),
                ('select_host', models.SmallIntegerField()),
                ('update_host', models.SmallIntegerField()),
                ('insert_host', models.SmallIntegerField()),
                ('delete_host', models.SmallIntegerField()),
                ('select_user', models.SmallIntegerField()),
                ('update_user', models.SmallIntegerField()),
                ('delete_user', models.SmallIntegerField()),
                ('insert_user', models.SmallIntegerField()),
                ('pub_ince', models.SmallIntegerField()),
                ('audit_ince', models.SmallIntegerField()),
                ('select_data', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'auth_privileges',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_group_name', models.CharField(max_length=50, unique=True)),
                ('user_group_jd', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'auth_user_group',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('user_pass', models.CharField(max_length=96)),
                ('email', models.EmailField(max_length=254)),
                ('lock_flag', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'auth_user_info',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
                ('comm', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_user_role',
            },
        ),
        migrations.AddField(
            model_name='userinfo',
            name='role',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_query_name='user_role_r', to='dbms.UserRole'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_group',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='dbms.UserGroup'),
        ),
    ]
