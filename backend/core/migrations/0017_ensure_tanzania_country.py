from django.db import migrations


def ensure_tanzania(apps, schema_editor):
    Country = apps.get_model('core', 'Country')

    Country.objects.update_or_create(
        code='TZA',
        defaults={
            'name': 'Tanzania',
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_seed_tanzania_country'),
    ]

    operations = [
        migrations.RunPython(
            ensure_tanzania,
            migrations.RunPython.noop,
        ),
    ]