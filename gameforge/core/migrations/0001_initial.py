# Generated by Django 5.2 on 2025-04-11 10:53

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GameConcept",
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
                ("title", models.CharField(max_length=200)),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("RPG", "RPG"),
                            ("FPS", "FPS"),
                            ("Strategy", "Strategy"),
                            ("Adventure", "Adventure"),
                            ("Horror", "Horror"),
                            ("Platformer", "Platformer"),
                            ("Puzzle", "Puzzle"),
                            ("Other", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                ("ambiance", models.CharField(max_length=200)),
                ("keywords", models.JSONField(default=list)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="game_concepts/"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GameCharacter",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("role", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "concept",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="characters",
                        to="core.gameconcept",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GameStory",
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
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "concept",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="story",
                        to="core.gameconcept",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GameUniverse",
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
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "concept",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="universe",
                        to="core.gameconcept",
                    ),
                ),
            ],
        ),
    ]
