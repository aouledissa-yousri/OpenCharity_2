# Generated by Django 4.2.7 on 2023-11-18 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipfsGateway', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='DonationCampaignIpfsGateway',
        ),
        migrations.RenameModel(
            old_name='Notification',
            new_name='DonationIpfsGateway',
        ),
        migrations.RenameModel(
            old_name='Donation',
            new_name='NotificationIpfsGateway',
        ),
        migrations.RenameModel(
            old_name='DonationCampaign',
            new_name='UserIpfsGateway',
        ),
        migrations.RenameField(
            model_name='donationcampaignipfsgateway',
            old_name='walletAddres',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='useripfsgateway',
            old_name='id',
            new_name='walletAddres',
        ),
    ]