# Generated by Django 4.1.3 on 2022-11-08 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkArrangement",
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
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("work", models.CharField(max_length=25, unique=True)),
                (
                    "work_type",
                    models.CharField(
                        choices=[("PT", "PART TIME"), ("FT", "FULL TIME")],
                        default="FT",
                        max_length=25,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EmployeeWorkArrangement",
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
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("percentage", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee.employee",
                    ),
                ),
                (
                    "work_arrangement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="work.workarrangement",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
