# Generated by Django 5.1.1 on 2024-09-30 21:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_document', models.FileField(upload_to='verification_docs/', verbose_name='ID Document')),
                ('verified', models.BooleanField(default=False, verbose_name='Verified')),
                ('verification_date', models.DateTimeField(blank=True, null=True, verbose_name='Verification Date')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
