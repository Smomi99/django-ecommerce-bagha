# Generated by Django 3.0.7 on 2020-10-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_color_size_variants'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variant',
            field=models.CharField(choices=[('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Size-Color', 'Size-Color')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]