# Generated by Django 4.2.2 on 2024-08-01 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0005_client_owner_message_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="mailing",
        ),
        migrations.AddField(
            model_name="mailing",
            name="message",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="mailing.message",
                verbose_name="Cообщение",
            ),
        ),
    ]