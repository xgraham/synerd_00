# Generated by Django 3.2.7 on 2021-10-25 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officename', models.CharField(max_length=125)),
                ('attribution', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizationname', models.CharField(max_length=125)),
                ('description', models.CharField(max_length=125)),
                ('datejoined', models.DateField()),
                ('address1', models.CharField(max_length=125)),
                ('address2', models.CharField(max_length=125)),
                ('city', models.CharField(max_length=125)),
                ('state', models.CharField(max_length=125)),
                ('zipcode', models.CharField(max_length=125)),
                ('phonenumber', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicename', models.CharField(max_length=125)),
                ('description', models.CharField(max_length=125)),
                ('premium', models.CharField(max_length=125)),
                ('allocation', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerD.service')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriptiontypename', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=125, unique=True)),
                ('middlename', models.CharField(max_length=125)),
                ('firstname', models.CharField(max_length=125)),
                ('lastname', models.CharField(max_length=125)),
                ('email', models.CharField(max_length=125)),
                ('address1', models.CharField(max_length=125)),
                ('address2', models.CharField(max_length=125)),
                ('city', models.CharField(max_length=125)),
                ('state', models.CharField(max_length=125)),
                ('zipcode', models.CharField(max_length=125)),
                ('employername', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='TransferredSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transferfrom', models.CharField(max_length=125)),
                ('transferto', models.CharField(max_length=125)),
                ('requestdate', models.DateField()),
                ('transferdate', models.DateField()),
                ('subscriberid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerD.subscriber')),
            ],
        ),
        migrations.AddField(
            model_name='subscriber',
            name='subscriptiontypecode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerD.subscriptiontype'),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerD.userinfo'),
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('nativecountry', models.CharField(max_length=125)),
                ('citizenship', models.CharField(max_length=125)),
                ('isdelegate', models.BooleanField()),
                ('organizationcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerD.organization')),
                ('subscriberid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerD.subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('officecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerD.office')),
                ('subscriberid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerD.subscriber')),
            ],
        ),
    ]
