# Generated by Django 4.0.3 on 2022-03-23 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inadimplentes', '0014_alter_inquilino_meses_de_inadimplencia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inquilino',
            old_name='meses_de_inadimplencia',
            new_name='inadimplencia',
        ),
    ]
