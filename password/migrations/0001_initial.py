# Generated by Django 3.1.5 on 2021-02-08 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth', models.CharField(help_text='Input Auth Level here. e.g: Admin, Peer, Acquaintance (max length = 50).', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=60)),
                ('firstName', models.CharField(max_length=50)),
                ('password', models.CharField(help_text='Input password here (max length = 100).', max_length=100)),
                ('email', models.EmailField(help_text='Input email address here (max length = 254).', max_length=254)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='password.authlevel')),
            ],
            options={
                'ordering': ['lastName', 'firstName'],
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountName', models.CharField(help_text='Input the name of the account (max length = 100).', max_length=100)),
                ('summary', models.CharField(help_text='Input summary of the account here (max length = 300).', max_length=300, null=True)),
                ('userID', models.CharField(help_text='Input the user id of the account (max length = 80).', max_length=80, null=True)),
                ('password', models.CharField(help_text='Input password of the account here (max length = 300).', max_length=300, null=True)),
                ('email', models.EmailField(help_text='Input email address of the account here (max length = 254).', max_length=254, null=True)),
                ('date_of_created', models.DateField(blank=True, null=True)),
                ('date_of_deleted', models.DateField(blank=True, null=True)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='password.authlevel')),
            ],
        ),
    ]
