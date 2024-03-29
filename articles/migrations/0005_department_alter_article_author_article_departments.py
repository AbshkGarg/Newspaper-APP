# Generated by Django 4.2.8 on 2024-01-19 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='article',
            name='departments',
            field=models.ManyToManyField(to='articles.department'),
        ),
    ]
