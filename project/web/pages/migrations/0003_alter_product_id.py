# Generated by Django 4.2.7 on 2023-11-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_product_photo_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(max_length=2, primary_key=True, serialize=False),
        ),
    ]