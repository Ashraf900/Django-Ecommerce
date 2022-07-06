# Generated by Django 4.0.5 on 2022-06-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_subcategory_product_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(max_length=30000)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
    ]
