# Generated by Django 4.2.6 on 2023-11-10 16:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AffectedProduct",
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
                ("vendor", models.CharField(max_length=512, null=True)),
                ("product", models.CharField(max_length=2048, null=True)),
                (
                    "collection_url",
                    models.CharField(default=None, max_length=2048, null=True),
                ),
                (
                    "package_name",
                    models.CharField(default=None, max_length=2048, null=True),
                ),
                ("repo", models.CharField(default=None, max_length=2048, null=True)),
                (
                    "default_status",
                    models.CharField(
                        choices=[
                            ("affected", "affected"),
                            ("unaffected", "unaffected"),
                            ("unknown", "unknown"),
                        ],
                        default="unknown",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CveRecord",
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
                (
                    "state",
                    models.CharField(
                        choices=[("PUBLISHED", "PUBLISHED"), ("REJECTED", "REJECTED")],
                        default="PUBLISHED",
                        max_length=9,
                    ),
                ),
                (
                    "cve_id",
                    models.CharField(
                        max_length=32,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^CVE-[0-9]{4}-[0-9]{4,19}$"
                            )
                        ],
                    ),
                ),
                ("serial", models.PositiveIntegerField(default=1)),
                ("date_updated", models.DateTimeField(default=None, null=True)),
                ("date_reserved", models.DateTimeField(default=None, null=True)),
                ("date_published", models.DateTimeField(default=None, null=True)),
                ("local_timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Description",
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
                (
                    "lang",
                    models.CharField(
                        default="en",
                        max_length=16,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[A-Za-z]{2,4}([_-][A-Za-z]{4})?([_-]([A-Za-z]{2}|[0-9]{3}))?$"
                            )
                        ],
                    ),
                ),
                ("value", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                (
                    "short_name",
                    models.CharField(default=None, max_length=32, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Platform",
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
                ("name", models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("vendor", models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name="SupportingMedia",
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
                ("_type", models.CharField(max_length=256)),
                ("base64", models.BooleanField(default=False)),
                ("value", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("value", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Version",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("affected", "affected"),
                            ("unaffected", "unaffected"),
                            ("unknown", "unknown"),
                        ],
                        default="unknown",
                        max_length=10,
                    ),
                ),
                ("version_type", models.CharField(max_length=128, null=True)),
                ("version", models.CharField(max_length=1024, null=True)),
                ("less_than", models.CharField(max_length=1024, null=True)),
                ("less_equal", models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Reference",
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
                ("url", models.CharField(max_length=2048)),
                ("name", models.CharField(max_length=512)),
                ("tags", models.ManyToManyField(to="shared.tag")),
            ],
        ),
        migrations.CreateModel(
            name="ProgramRoutine",
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
                ("name", models.CharField(max_length=4096)),
                (
                    "_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="program_routines",
                        to="shared.affectedproduct",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProgramFile",
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
                ("name", models.CharField(max_length=1024)),
                (
                    "_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="program_files",
                        to="shared.affectedproduct",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProblemType",
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
                (
                    "cwe_id",
                    models.CharField(
                        max_length=9,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator("^CWE-[1-9][0-9]*$")
                        ],
                    ),
                ),
                ("_type", models.CharField(max_length=128, null=True)),
                ("description", models.ManyToManyField(to="shared.description")),
                ("references", models.ManyToManyField(to="shared.reference")),
            ],
        ),
        migrations.CreateModel(
            name="NixIssue",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("U", "unknown"),
                            ("A", "affected"),
                            ("NA", "notaffected"),
                            ("O", "notforus"),
                            ("W", "wontfix"),
                        ],
                        default="U",
                        max_length=2,
                    ),
                ),
                ("cve", models.ManyToManyField(to="shared.cverecord")),
                (
                    "description",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="shared.description",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NixEvent",
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
                ("reference", models.TextField()),
                (
                    "issue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shared.nixissue",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NixAdvisory",
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
                ("issues", models.ManyToManyField(to="shared.nixissue")),
            ],
        ),
        migrations.CreateModel(
            name="Module",
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
                ("name", models.CharField(max_length=4096)),
                (
                    "_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="modules",
                        to="shared.affectedproduct",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Metric",
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
                ("format", models.CharField(max_length=64)),
                ("content", models.JSONField()),
                ("scenarios", models.ManyToManyField(to="shared.description")),
            ],
        ),
        migrations.CreateModel(
            name="Impact",
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
                (
                    "capec_id",
                    models.CharField(
                        max_length=11,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^CAPEC-[1-9][0-9]{0,4}$"
                            )
                        ],
                    ),
                ),
                ("description", models.ManyToManyField(to="shared.description")),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("time", models.DateTimeField()),
                (
                    "description",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shared.description",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="description",
            name="media",
            field=models.ManyToManyField(to="shared.supportingmedia"),
        ),
        migrations.AddField(
            model_name="cverecord",
            name="assigner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assigned",
                to="shared.organization",
            ),
        ),
        migrations.AddField(
            model_name="cverecord",
            name="requester",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="requested",
                to="shared.organization",
            ),
        ),
        migrations.CreateModel(
            name="Credit",
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
                (
                    "_type",
                    models.CharField(
                        choices=[
                            ("finder", "finder"),
                            ("reporter", "reporter"),
                            ("analyst", "analyst"),
                            ("coordinator", "coordinator"),
                            ("remediation developer", "remediation developer"),
                            ("remediation reviewer", "remediation reviewer"),
                            ("remediation verifier", "remediation_verifier"),
                            ("tool", "tool"),
                            ("sponsor", "sponsor"),
                            ("other", "other"),
                        ],
                        default="finder",
                        max_length=21,
                    ),
                ),
                (
                    "description",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shared.description",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="shared.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cpe",
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
                (
                    "name",
                    models.CharField(
                        default=None,
                        max_length=2048,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "([c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9._\\-~%]*){0,6})|(cpe:2\\.3:[aho*\\-](:(((\\?*|\\*?)([a-zA-Z0-9\\-._]|(\\\\[\\\\*?!\"#$%&'()+,/:;<=>@\\[\\]\\^`{|}~]))+(\\?*|\\*?))|[*\\-])){5}(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[*\\-]))(:(((\\?*|\\*?)([a-zA-Z0-9\\-._]|(\\\\[\\\\*?!\"#$%&'()+,/:;<=>@\\[\\]\\^`{|}~]))+(\\?*|\\*?))|[*\\-])){4})"
                            )
                        ],
                    ),
                ),
                (
                    "_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cpes",
                        to="shared.affectedproduct",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Container",
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
                (
                    "_type",
                    models.CharField(
                        choices=[
                            ("cna", "CVE Numbering Authority"),
                            ("adp", "Authorized Data Publisher"),
                        ],
                        default="cna",
                        max_length=3,
                    ),
                ),
                ("title", models.CharField(default=None, max_length=256, null=True)),
                ("date_assigned", models.DateTimeField(default=None, null=True)),
                ("date_public", models.DateTimeField(default=None, null=True)),
                ("source", models.JSONField(default=dict)),
                ("affected", models.ManyToManyField(to="shared.affectedproduct")),
                (
                    "configurations",
                    models.ManyToManyField(
                        related_name="container_configurations", to="shared.description"
                    ),
                ),
                ("credits", models.ManyToManyField(to="shared.credit")),
                (
                    "cve",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shared.cverecord",
                    ),
                ),
                ("descriptions", models.ManyToManyField(to="shared.description")),
                (
                    "exploits",
                    models.ManyToManyField(
                        related_name="container_exploits", to="shared.description"
                    ),
                ),
                ("metrics", models.ManyToManyField(to="shared.metric")),
                ("problem_types", models.ManyToManyField(to="shared.problemtype")),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shared.organization",
                    ),
                ),
                ("references", models.ManyToManyField(to="shared.reference")),
                (
                    "solutions",
                    models.ManyToManyField(
                        related_name="container_solutions", to="shared.description"
                    ),
                ),
                ("tags", models.ManyToManyField(to="shared.tag")),
                ("timeline", models.ManyToManyField(to="shared.event")),
                (
                    "workarounds",
                    models.ManyToManyField(
                        related_name="container_workarounds", to="shared.description"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="affectedproduct",
            name="platforms",
            field=models.ManyToManyField(to="shared.platform"),
        ),
        migrations.AddField(
            model_name="affectedproduct",
            name="versions",
            field=models.ManyToManyField(to="shared.version"),
        ),
    ]
