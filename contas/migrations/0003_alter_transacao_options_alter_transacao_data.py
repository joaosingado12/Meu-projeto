# Generated by Django 4.2.3 on 2023-07-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contas", "0002_transacao"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transacao",
            options={"verbose_name_plural": "Transaçoes"},
        ),
        migrations.AlterField(
            model_name="transacao",
            name="data",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
