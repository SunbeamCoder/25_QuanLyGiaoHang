# Generated by Django 4.1.3 on 2023-05-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_rider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='xe',
            field=models.CharField(choices=[('Xe số', 'Xe số'), ('Xe tay ga', 'Xe tay ga'), ('oto', 'oto')], default='Xe số', max_length=50),
        ),
    ]