# Generated by Django 4.2.6 on 2023-12-05 02:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("shared", "0002_remove_cpe__product_remove_module__product_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="NixIssue",
            new_name="NixpkgsIssue",
        ),
        migrations.RenameModel(
            old_name="NixAdvisory",
            new_name="NixpkgsAdvisory",
        ),
        migrations.RenameModel(
            old_name="NixEvent",
            new_name="NixpkgsEvent",
        ),
        migrations.AlterField(
            model_name="nixpkgsadvisory",
            name="issues",
            field=models.ManyToManyField(to="shared.nixpkgsissue"),
        ),
        migrations.AlterField(
            model_name="nixpkgsevent",
            name="issue",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="shared.nixpkgsissue"
            ),
        ),
        migrations.AddField(
            model_name="nixpkgsissue",
            name="created",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="nixpkgsissue",
            name="code",
            field=models.CharField(default="NIXPKGS-1234-12345", max_length=32),
            preserve_default=False,
        ),
    ]