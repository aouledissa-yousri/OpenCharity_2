# Generated by Django 3.2.21 on 2023-11-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfsGateway', '0003_rename_walletaddres_useripfsgateway_walletaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationipfsgateway',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
