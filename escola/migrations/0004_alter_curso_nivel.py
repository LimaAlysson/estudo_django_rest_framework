# Generated by Django 5.0.3 on 2025-03-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_alter_curso_nivel_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('A', 'Avançado'), ('B', 'Básico'), ('I', 'Intermediário')], default='B', max_length=1),
        ),
    ]
