# Generated by Django 4.0.3 on 2022-03-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inadimplentes', '0012_alter_inquilino_valor_do_aluguel'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquilino',
            name='meses_de_inadimplencia',
            field=models.CharField(default='ADIMPLENTE', max_length=255),
        ),
    ]
