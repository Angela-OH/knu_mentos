# Generated by Django 3.0 on 2021-07-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('모름', '모름'), ('ISTJ', 'ISTJ'), ('ISFJ', 'ISFJ'), ('INFJ', 'INFJ'), ('INTJ', 'INTJ'), ('ISTP', 'ISTP'), ('ISFP', 'ISFP'), ('INFP', 'INFP'), ('INTP', 'INTP'), ('ESTP', 'ESTP'), ('ESFP', 'ESFP'), ('ENFP', 'ENFP'), ('ENTP', 'ENTP'), ('ESTJ', 'ESTJ'), ('ESFJ', 'ESFJ'), ('ENFJ', 'ENFJ'), ('ENTJ', 'ENTJ')], default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(default='', max_length=15, null=True),
        ),
    ]