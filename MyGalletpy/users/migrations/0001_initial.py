# Generated by Django 4.0.3 on 2022-04-25 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id_transaction', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_transaction', models.DateField()),
                ('type_transaction', models.BooleanField(default=True)),
                ('amount', models.FloatField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Pocket_transaction',
            fields=[
                ('id_pocket', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id_pocket', models.BigAutoField(primary_key=True, serialize=False)),
                ('name_pocket', models.CharField(max_length=30)),
                ('balance_pocket', models.FloatField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Normal_transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('id_transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.transaction')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
