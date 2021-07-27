# Generated by Django 2.1.15 on 2021-06-10 18:50

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodeodm', '0008_rename_default_odm_node'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processingnode',
            options={'verbose_name': 'Processing Node', 'verbose_name_plural': 'Processing Nodes'},
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='api_version',
            field=models.CharField(help_text='API version used by the node', max_length=32, null=True, verbose_name='API Version'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='available_options',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, help_text='Description of the options that can be used for processing', verbose_name='Available Options'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='engine',
            field=models.CharField(help_text='Engine used by the node.', max_length=255, null=True, verbose_name='Engine'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='engine_version',
            field=models.CharField(help_text='Engine version used by the node.', max_length=32, null=True, verbose_name='Engine Version'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='hostname',
            field=models.CharField(help_text='Hostname or IP address where the node is located (can be an internal hostname as well). If you are using Docker, this is never 127.0.0.1 or localhost. Find the IP address of your host machine by running ifconfig on Linux or by checking your network settings.', max_length=255, verbose_name='Hostname'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='label',
            field=models.CharField(blank=True, default='', help_text='Optional label for this node. When set, this label will be shown instead of the hostname:port name.', max_length=255, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='last_refreshed',
            field=models.DateTimeField(help_text='When was the information about this node last retrieved?', null=True, verbose_name='Last Refreshed'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='max_images',
            field=models.PositiveIntegerField(blank=True, help_text='Maximum number of images accepted by this node.', null=True, verbose_name='Max Images'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='port',
            field=models.PositiveIntegerField(help_text="Port that connects to the node's API", verbose_name='Port'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='queue_count',
            field=models.PositiveIntegerField(default=0, help_text='Number of tasks currently being processed by this node (as reported by the node itself)', verbose_name='Queue Count'),
        ),
        migrations.AlterField(
            model_name='processingnode',
            name='token',
            field=models.CharField(blank=True, default='', help_text="Token to use for authentication. If the node doesn't have authentication, you can leave this field blank.", max_length=1024, verbose_name='Token'),
        ),
    ]