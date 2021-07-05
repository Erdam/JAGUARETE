# Generated by Django 3.2.4 on 2021-06-24 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JAGUARETE', '0002_auto_20210622_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='_img'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JAGUARETE.categoria'),
        ),
        migrations.DeleteModel(
            name='Categorias',
        ),
    ]