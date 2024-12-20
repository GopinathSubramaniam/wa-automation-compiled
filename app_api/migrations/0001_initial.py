# Generated by Django 5.0.7 on 2024-11-11 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, unique=True)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_app_setting',
            },
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(null=True)),
                ('completed_on', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=150)),
                ('total_contact', models.SmallIntegerField(default=0)),
                ('total_success', models.SmallIntegerField(default=0)),
                ('status', models.SmallIntegerField(default=0)),
                ('msg', models.TextField(null=True)),
                ('err_msg', models.CharField(max_length=255, null=True)),
                ('img_path', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tbl_campaign',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_group',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('file_name', models.CharField(max_length=200, unique=True)),
                ('desc', models.TextField(null=True)),
                ('type', models.CharField(default='I', max_length=1)),
            ],
            options={
                'db_table': 'tbl_template',
            },
        ),
        migrations.CreateModel(
            name='TemplateSync',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='I', max_length=1)),
                ('msg', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_template_sync',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=151)),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.SmallIntegerField(default=3)),
                ('country_code', models.CharField(default=91, max_length=5)),
            ],
            options={
                'db_table': 'tbl_user',
            },
        ),
        migrations.CreateModel(
            name='CampaignDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('sent', models.BooleanField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.campaign')),
            ],
            options={
                'db_table': 'tbl_campaign_detail',
            },
        ),
        migrations.AddField(
            model_name='campaign',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.group'),
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.user'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=151)),
                ('city', models.CharField(max_length=15, null=True)),
                ('state', models.CharField(max_length=15, null=True)),
                ('mobile', models.CharField(max_length=15)),
                ('tags', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
                ('whatsapp_enabled', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.user')),
            ],
            options={
                'db_table': 'tbl_contact',
                'unique_together': {('mobile', 'user')},
            },
        ),
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('dir', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_api.user')),
            ],
            options={
                'db_table': 'tbl_user_session',
            },
        ),
        migrations.CreateModel(
            name='GroupContactMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.contact')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.user')),
            ],
            options={
                'db_table': 'tbl_group_contact_map',
                'unique_together': {('group', 'contact')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('name', 'user')},
        ),
    ]
