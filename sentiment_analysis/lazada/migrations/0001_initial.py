# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', models.CharField(max_length=20)),
                ('comment_rating', models.FloatField()),
                ('detail', models.CharField(max_length=500)),
                ('nickname', models.CharField(max_length=200)),
                ('id_rating_review', models.IntegerField()),
                ('fk_customer', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('title', models.CharField(max_length=300)),
                ('votes_up', models.IntegerField()),
                ('votes_down', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('price_final', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('image_url', models.CharField(max_length=200)),
                ('link_product', models.CharField(max_length=200)),
                ('product_rating', models.IntegerField()),
                ('product_vote_total', models.IntegerField()),
                ('sku', models.CharField(max_length=20)),
                ('vendor', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(to='lazada.Product'),
            preserve_default=True,
        ),
    ]
