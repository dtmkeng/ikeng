# Generated by Django 3.2.4 on 2021-07-29 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comment', to='core.post')),
            ],
        ),
    ]
