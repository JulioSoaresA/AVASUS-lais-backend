# Generated by Django 4.0.5 on 2022-07-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_usuarios_indica_privacidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='indica_privacidade',
            field=models.TextField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default=0, max_length=3, null=True, verbose_name='Privacidade'),
        ),
    ]