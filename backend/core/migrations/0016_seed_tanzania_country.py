from django.db import migrations


def seed_tanzania(apps, schema_editor):
    Country = apps.get_model('core', 'Country')

    Country.objects.update_or_create(
        code='TZA',
        defaults={
            'name': 'Tanzania',
        },
    )


def unseed_tanzania(apps, schema_editor):
    # Intentionally keep Tanzania when reversing this migration.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_user_phone'),
    ]

    operations = [
        migrations.RunPython(seed_tanzania, unseed_tanzania),
    ]