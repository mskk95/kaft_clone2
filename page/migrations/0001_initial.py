# Generated by Django 2.2.4 on 2019-08-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('cover_image', models.ImageField(upload_to='page')),
                ('status', models.CharField(choices=[('draft', 'draft'), ('published', 'published'), ('deleted', 'deleted')], default='draft', max_length=11)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
