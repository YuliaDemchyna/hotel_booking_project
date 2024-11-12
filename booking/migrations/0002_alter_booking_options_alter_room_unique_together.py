# Generated by Django 5.1.3 on 2024-11-11 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('hotel', 'room_number')},
        ),
    ]