# Generated by Django 4.0.5 on 2022-07-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0018_alter_atividades_nome_componente'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividades',
            name='nome_curso',
            field=models.CharField(max_length=150, null=True, verbose_name='Nome do curso'),
        ),
    ]