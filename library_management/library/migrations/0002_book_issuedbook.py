# Generated by Django 4.1.1 on 2022-09-10 05:37

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bookno', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('education', 'Education'), ('entertainment', 'Entertainment'), ('comics', 'Comics'), ('biography', 'Biography'), ('history', 'History'), ('novel', 'Novel'), ('fantasy', 'Fantasy'), ('thriller', 'Thriller'), ('scifi', 'Sci-Fi')], default='education', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment', models.CharField(max_length=30)),
                ('bookno', models.CharField(max_length=30)),
                ('issuedate', models.DateField(auto_now=True)),
                ('expirydate', models.DateField(default=library.models.get_expiry)),
            ],
        ),
    ]
