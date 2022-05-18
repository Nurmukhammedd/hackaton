# Generated by Django 3.2.7 on 2022-05-18 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Brand')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='maker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.brand'),
        ),
        migrations.DeleteModel(
            name='Maker',
        ),
    ]
