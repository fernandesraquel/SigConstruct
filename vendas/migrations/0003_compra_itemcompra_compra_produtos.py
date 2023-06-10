# Generated by Django 4.2.1 on 2023-06-09 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('vendas', '0002_produto_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.compra')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.produto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='produtos',
            field=models.ManyToManyField(through='vendas.ItemCompra', to='vendas.produto'),
        ),
    ]