# Generated by Django 4.0.6 on 2023-07-13 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qnas', '0002_alter_answer_question_alter_question_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='writer',
            field=models.TextField(verbose_name='작성자'),
        ),
        migrations.AlterField(
            model_name='question',
            name='writer',
            field=models.TextField(verbose_name='작성자'),
        ),
    ]
