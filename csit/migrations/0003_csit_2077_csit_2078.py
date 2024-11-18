# Generated by Django 5.1.3 on 2024-11-13 00:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("csit", "0002_csit_2079"),
    ]

    operations = [
        migrations.CreateModel(
            name="Csit_2077",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("dob", models.CharField(max_length=30)),
                ("symbol", models.CharField(max_length=20)),
                ("reg", models.CharField(max_length=50)),
                ("mob", models.CharField(max_length=10)),
                ("add", models.CharField(max_length=60)),
                ("guardian", models.CharField(max_length=50)),
                ("prof", models.CharField(max_length=50)),
                ("mobs", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "csit2077",
            },
        ),
        migrations.CreateModel(
            name="Csit_2078",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("dob", models.CharField(max_length=30)),
                ("symbol", models.CharField(max_length=20)),
                ("reg", models.CharField(max_length=50)),
                ("mob", models.CharField(max_length=10)),
                ("add", models.CharField(max_length=60)),
                ("guardian", models.CharField(max_length=50)),
                ("prof", models.CharField(max_length=50)),
                ("mobs", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "csit2078",
            },
        ),
    ]
